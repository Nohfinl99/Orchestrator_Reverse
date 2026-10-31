# Chọn tác vụ nhận thức và context theo mục tiêu

Thiết kế từ cuộc họp ngày 31/10/2026. Các phiên review thật thống nhất xây lớp chọn tác vụ/tài liệu nhỏ; đây là hướng dẫn sử dụng và thiết kế tích hợp, chưa phải loader hoặc runtime dispatch. Mười stack và mười protocol gốc giữ nguyên byte. Các tên CT dưới đây là mục lục thao tác, không thay identity, phase, gate hay schema đã có.

Vấn đề cần giải quyết là nạp lại context/skill không cần thiết và lặp việc chưa có tiến triển. Quan sát được phần contract chung lặp trong tài liệu; chưa có trace chứng minh active loader đang gọi lặp các stack. Vì vậy không gán nguyên nhân runtime từ sự giống nhau của file.

## Một vòng công việc

`objective → chọn CT/owner → chọn nguồn tối thiểu → kiểm prerequisite → tạo artifact → review độc lập → ghi delta và next/stop`

Mỗi task giữ objective, owner, input path/revision/digest, output, acceptance, dependencies, ngân sách và điều kiện dừng theo [routing protocol](../../../prompt_stacks/protocols/routing_protocol.md). Lưu original request; kết quả truy xuất/graph chỉ là dữ liệu tham khảo. Không replay cả lịch sử vào mỗi prompt. Thiếu applicability/authority/ACK/pair ở nhánh phụ thuộc thì giữ chờ, không bỏ kiểm để giảm context.

| CT / mục tiêu | Owner trách nhiệm | Chỉ mở khi cần | Artifact / reviewer |
|---|---|---|---|
| CT-01 Hiểu yêu cầu, chọn scope và DAG | Prompt-Master | [00 intake](../../../prompt_stacks/00_bootstrap.md), [baseline](../../../prompt_stacks/protocols/baseline_protocol.md) | Task packet với input/output/acceptance; Evidence-Synthesizer kiểm nguồn |
| CT-02 Tìm, đối chiếu và trích kiến thức | Evidence-Synthesizer | [knowledge](../../../prompt_stacks/protocols/knowledge_protocol.md), card có liên quan | Unit/locator/condition/conflict; reviewer khác producer; chưa admission/ACK thì giữ candidate |
| CT-03 Phân tích target | Triage-Sentinel → Decomp-Analyst; Crypto khi có evidence phù hợp | [pair](../../../prompt_stacks/protocols/pair_protocol.md), stack chuyên trách | Evidence đúng target/component/slice/IDB state; Evidence-Synthesizer review; không chạy trong task tài liệu này |
| CT-04 Thiết kế/sửa theo roadmap | Prompt-Master chọn owner đã map; Product-Evolution-Architect làm proposal khi đúng objective | Specification và exact source của một caller; [state](../../../prompt_stacks/protocols/state_protocol.md) khi thay state | Candidate revision/diff; reviewer chuyên môn khác producer. Product dispatch chưa bind thì không giả executable owner |
| CT-05 Review logic/security/evidence | Evidence-Synthesizer; Prompt-Master xử lý dependency | [evaluation](../../../prompt_stacks/protocols/evaluation_protocol.md); [Cloudflare chọn lọc](cloudflare.md) chỉ khi security-relevant | Finding/objection/decision có locator và scope; consensus không thay evidence |
| CT-06 Bàn giao, resume, tiếp tục/dừng | Prompt-Master + Evidence-Synthesizer | [handoff](../../../prompt_stacks/protocols/handoff_protocol.md), [Paperclip sync](paperclip-sync.md) khi có tích hợp | Delta, artifact digest, remaining gap, next owner; revalidate upstream/ACK khi resume |

Triage/Decomp/Crypto không bị gọi cho việc sắp tài liệu. Training/pilot/release chỉ được mở theo objective và prerequisites riêng, không vì đến lượt stack W6/W7 trong danh sách.

## Chọn model và skill

Theo chỉ thị người dùng: GPT-6.1 nhận thiết kế khó, review logic/security, evidence mâu thuẫn và thay đổi chạm quyền/state. GPT-6 Luna hỗ trợ inventory, tìm locator, sắp xếp và code nhỏ theo roadmap/acceptance rõ, sau đó model cao review. Không dùng độ dài diff làm thước đo rủi ro. Đây là phân công người dùng chọn, chưa là benchmark hay cấu hình router đã deploy.

Mỗi task ghi một owner chính và reviewer khác producer. Model là lựa chọn thực thi trong phạm vi role hiện hữu, không tạo identity mới. Chỉ mở SKILL.md liên quan rồi section cần dùng; không nạp toàn catalog/reference. Reading Companion dùng khi trích/biểu diễn tri thức; REA/IDA dùng khi task cần phân tích artifact/target; Cloudflare dùng khi có câu hỏi security boundary. Catalog không phải nội dung prompt phải gửi hết.

Packet context tối thiểu gồm: objective/scope; nguyên lý và gate áp dụng; selected CT; input locators/digests và đoạn cần đọc; unresolved/conflict; output/acceptance; budget/stop; reviewer/next. Những mục này là các nhóm cần có, không phải giới hạn số lượng cố định hoặc token cap của model.

Ngân sách context phải ghi đơn vị: byte UTF-8 của navigation query khác model tokens. Công cụ local kiểm byte cho JSON kết quả, không bảo đảm toàn prompt nằm trong context window. Nếu quá lớn: thu hẹp objective, truy xuất đoạn có locator hoặc chia task giữ dependencies; không bỏ conditions/FAIL/authority requirement. Node bị loại vì budget phải được ghi omitted, không tính covered. Query graph không tự chọn full dependency closure hoặc đồng bộ admission; owner vẫn phải kiểm protocol gốc.

## Tránh vòng lặp vô ích

Fingerprint công việc gồm objective + caller/action + input/context/dependency revisions + failure signature. Đổi tên task hoặc timestamp không là tiến triển. Delta hợp lệ phải chỉ ra artifact/evidence mới, giả thuyết bị bác bỏ, prerequisite đã được chứng minh hoặc gap được thu hẹp có locator.

- Cùng signature, không có delta: STOP nhánh và ghi điều kiện mở lại; không gọi lại skill/model để lặp câu trả lời.
- Upstream/source/context/IDB revision đổi: revalidate hoặc invalidate downstream và ACK theo contract, tạo revision/attempt mới.
- Tối đa hai vòng review tài liệu trong task/candidate theo contract gốc; hết cap mà chưa đạt thì giữ REVISE_NOT_ACCEPTED, lưu conflict và owner quyết định. Finding khác không tự reset cap hoặc ép consensus.
- Numeric runtime caps cho calls/cost/time/retry phải được xác định trong packet runtime riêng; hai vòng review tài liệu không là runtime budget.

Lớp này không thay P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Nguồn chuẩn: [kiến trúc](../../architecture/system.md), [sáu role](../../architecture/agents.md), [phase map](../../planning/phase-map.md), [knowledge policy v2](../../knowledge/knowledge-policy-v2.md).

Knowledge graph và biên bản đầy đủ là LOCAL_ONLY trong workspace cha: `knowledge_graph/` và `evidence/orchestrator_meetings/20261031_context_sync_01/`. Clone public không có các file đó. Không cần tải corpus local để dùng hướng dẫn này.
