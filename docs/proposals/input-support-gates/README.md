# Input support: đề xuất checkpoint theo bằng chứng — revision 1

Ngày 24/10/2026. Scope được người dùng chọn: chuẩn bị và verify packet offline; chọn benchmark có raw hoặc kết quả pentest có nguồn, ưu tiên static REA. Người dùng giao chọn model theo tác vụ khi tới bước chạy: suy luận cho roadmap/pentest/phân tích khó; khả năng lập trình phù hợp cho code hẹp. Hiện chưa cấp một provider call, upload dữ liệu hay numeric runtime budget cụ thể.

Đây là bốn checkpoint đề xuất cho nhánh input-support, không thay G1–G4, W0–W7 hoặc R0–R6. Tiêu chí/threshold chờ người dùng quyết định; tỷ lệ hiện tại phản ánh tiêu chí có bằng chứng trong scope đã ghi, không phải xác suất thành công hoặc điểm model tự chấm.

## Cách tính và quyết định

Mỗi checkpoint có 6 tiêu chí trọng số bằng nhau. Tỷ lệ = số tiêu chí VERIFIED / 6 × 100; PENDING/NOT_RUN/FAILED đều không cộng điểm. Luôn báo riêng số chưa kiểm và số fail; 0% NOT_RUN không có nghĩa đã test rồi thất bại. Không gộp bốn checkpoint thành một phần trăm toàn dự án. Thay mẫu số phải tạo revision mới và giữ kết quả cũ.

Đề xuất: chỉ nhận checkpoint khi 6/6 được verify, critical invariants không fail và anh chấp nhận scope/criteria. Anh có thể điều chỉnh ngưỡng bằng quyết định có revision; không dùng ngưỡng thấp để bỏ qua source integrity, intent preservation hoặc quyền. Self-review/hash check không thay review độc lập hoặc behavioral evidence. [Status](status.json) là worksheet báo cáo, không phải API/gate engine runtime.

## Bốn checkpoint

| Checkpoint | Sáu tiêu chí cố định ở revision này | Căn cứ để đóng |
|---|---|---|
| INPUT-A — chốt mục tiêu và packet | A1 scope/clarifications được ghi; A2 một consumer/call site có pin; A3 case/input/oracle được review đúng scope; A4 offline action/output/numeric budget/stop được ghi; A5 có raw model-refusal hoặc quyết định rõ chỉ benchmark năng lực đọc nguồn; A6 anh chốt criteria/threshold | Packet + nguồn + decision/review record thật; chuẩn bị file không tự xác nhận A3/A5/A6 |
| KNOWLEDGE-B — nguồn và admission | B1 captures khớp SHA/size; B2 phân biệt release/package/skill revision từ metadata; B3 capability inventory có provenance và chỉ rõ observation scope; B4 source-rights/applicability được review cho bundle; B5 actual consumer ACK bind context/bundle/digest; B6 review/admission độc lập theo scope | Read/hash chỉ đóng B1, đối chiếu metadata chỉ đóng B2/B3; không tự đóng G2 |
| IMPLEMENTATION-C — input pipeline giữ nghĩa | C1 adapter được source-map/integrate đúng caller; C2 giữ original input và version/digest; C3 rejection taxonomy được thực thi đúng layer; C4 normalization hiển thị diff và giữ ý định/raw locators; C5 ambiguity hỏi 2–3 câu, không bịa facts/authority; C6 negative/positive behavioral cases có raw và review | Code đã bind + accepted applicable R4a trước fixture + raw/R4b; proposal tài liệu không cộng điểm implementation |
| EVALUATION-D — benchmark model/REA thực | D1 model/provider/version/data policy/numeric cap cụ thể; D2 cases/oracles/input được adjudicate và freeze R4a; D3 environment/capability/authority và applicable pair đủ; D4 attempt có capture thật; D5 reviewer R4b khác producer/executor; D6 đạt metrics được anh nhận và có continuation/rollback decision | Benchmark mới đúng scope; không tái dùng PASS cũ làm permission hoặc kết quả cho task mới |

## Việc sửa ngay trong lượt này

1. Lưu [packet](packet.md), objective/budget và selected call site; ghi các input SHA/revision local, không sửa archive.
2. Kiểm lại captures REA, phiên bản và tool metadata; chỉ tính custody/metadata, chưa runtime admission.
3. Đọc lại raw benchmark tooling lịch sử và thiết kế [benchmark plan](benchmark-plan.md) có ground truth tách khỏi active KB. AO pentest hiện là thiết kế NOT_RUN, không lấy làm pentest result.
4. Ghi quy tắc bám ngữ cảnh và verification vào AGENTS/workflow. Không mặc định phát biểu của anh là fact; ghi đâu là objective/quyết định, đâu là claim cần kiểm, và nguồn nào có thể phản chứng.

Scope hiện tại có 0 target/provider/training/fixture calls mới; static reading không cần chạy REA chỉ để kiểm source repository. Target/native pentest mới cần target/action/pair và prerequisite riêng. Nạp reference đã có vào context để đọc được phép trong scope; training, weights, provider upload và runtime ACK là các hành động riêng.

## Điều phối và độ sâu

Prompt-Master phụ trách objective/DAG và kế hoạch model; Evidence-Synthesizer phụ trách support/conflict/review khi có phiên thật. Không khai các role này đã tham gia một cuộc họp nếu chưa dispatch. Tác vụ khó có phân tích phương án, phản chứng, dependency và điều kiện dừng; tác vụ hẹp rõ có thể đọc/kiểm trực tiếp. Thời gian dài hoặc model suy luận cao không thay evidence.

Khi được giao run thật, chọn model hiện có theo context/tool support, data constraints, khả năng reasoning/coding và budget tại thời điểm đó, ghi exact model ID/version/effort nếu hỗ trợ. Không gán “GPT/Gemini” một cách chung chung làm profile thực thi; không dùng taxonomy model để giả lập việc đổi model của phiên hiện tại.

## Trạng thái dự án kế thừa

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Snapshot kết quả từng checkpoint ở status.json và báo cáo phiên; current worksheet chưa được anh chấp nhận nên mọi checkpoint giữ DECISION_PENDING ngay cả khi có tiêu chí đã verify.
