# Đề xuất cải tiến từ nền tảng — 23/10/2026

**Revision 1 — DOCUMENT_FOUNDATION_IMPLEMENTED / RUNTIME_PROPOSED.** Người dùng giao: trích xuất phần hữu ích từ Orchestrator_Reverse trên GitHub vào folder hiện tại, cải tiến từ nền tảng, xuất bản và báo tiến trình. Đây là biên bản desk review và đề xuất viết lại lớp hướng dẫn làm việc; phiên Codex hiện tại là producer/self-reviewer. Chưa có cuộc họp nhiều agent hoặc review độc lập được thực hiện.

## Vấn đề cần giải quyết

Repo đã có 12 knowledge card và D01–D11, nhưng người điều phối vẫn cần tự nối chúng với task packet, consumer, evidence và điều kiện dừng. Folder local có thêm candidate routing/ghép prompt; theo hồ sơ đối chiếu local, candidate chưa tích hợp broker/runtime và nhận nhiều trạng thái do caller cung cấp. Đổi prompt hoặc thêm card chưa chứng minh admission hoặc enforcement thực.

Mục tiêu bản đầu: tạo một đường làm việc đọc được từ yêu cầu → chọn nguồn → lập task → xét prerequisite → handoff → báo tiến độ; đồng thời chỉ rõ nơi cần integration thật. Nguyên lý nằm ở [CONTEXT_VI](../../../CONTEXT_VI.md), ownership/boundary ở [system](../../architecture/system.md), gate ở [W4 readiness](../../planning/w4-readiness-plan.md). Các trang này giữ thẩm quyền hiện hữu; proposal này không tạo contract runtime mới.

## Nguồn và cách tận dụng

GitHub main được kiểm tại `1f9445f8d8c9ef13fd51c499c9df8003e1f9a9f1`; checkout khởi đầu `a69d9c030b7533df4779bfa198025abec13a42e0` từ nhánh Muse đã public. Phần knowledge đã có local nên tận dụng bằng bảng áp dụng mới, không sao chép lại 12 card. [Reuse map](reuse-map.md) ghi selected/rejected và nơi áp dụng; [manifest nguồn](../../../metadata/knowledge-foundation-source-pins.json) giữ revision/digest và read scope. Các nguồn S1/S2/S3 vẫn dùng commit/rights đã pin trong catalog gốc; không tuyên bố đọc lại toàn upstream hoặc quyền mới.

## Quyết định tư vấn

1. Viết lại lớp hướng dẫn thao tác bằng [operating guide](operating-guide.md) và [worksheet task/handoff](packet-template.md). Đây là đầu ra tài liệu có thể dùng ngay cho proposal/review.
2. Giữ REA workflow/evidence/ledger và IDA native/decompiler/IDB-state xuyên suốt mọi boundary applicable. Phân biệt knowledge phương pháp với observation của target; ACK của KB không thay ACK của target pair hoặc action authority.
3. Giữ D01–D11 với đúng phạm vi disposition. Ví dụ jailbreak/tool copy không cấp authority; self-score/JSON parse/stars không đóng gate. Có thể nghiên cứu một chủ đề khi task phù hợp, nhưng không biến lời khuyên ngoài thành policy project.
4. Thiết kế tiếp admission cho một consumer/call site bằng source projection có sẵn. Applicability phải có căn cứ từ task/policy; không lấy cờ caller tự khai làm bằng chứng miễn pair hoặc miễn knowledge validation.
5. Xuất bản bản tài liệu qua nhánh review. Thay đổi API, runtime, registry, rights hoặc code phụ thuộc B4 cần packet/compatibility riêng. Nguyên bản archive, mười stack/protocol và lịch sử FAIL được bảo toàn.

## Lộ trình từ folder

Các bước dưới là thứ tự proposal cải tiến, không thay hệ R0–R6, W0–W7 hoặc G1–G4.

| Bước | Output và owner trách nhiệm | Điều kiện nhận | Tiến độ |
|---|---|---|---|
| Chọn và bind nguồn | Reuse map + source pins; Prompt-Master, Evidence-Synthesizer review khi có phiên thật | Mỗi ý có nguồn/revision, giới hạn và ứng dụng cụ thể | Đã viết, self-review |
| Hướng dẫn làm việc từ đầu | Guide + worksheet + entry/navigation | Tìm được đầu vào/đầu ra/stop/handoff; links và preservation được kiểm IA | Đã viết; kiểm/publish ghi ở báo cáo phiên |
| Một consumer admission | Compatibility packet dựa projection hiện có | Call site/action cụ thể, source bindings, validator/receipt producers, output/budget, reviewer thật | PROPOSED_NOT_DISPATCHED |
| Sửa code đúng boundary | Candidate revision + compatibility review | B4 correction riêng trước phần phụ thuộc; source mapping, scope và accepted R4a trước fixture | Chưa triển khai trong lượt này |
| Knowledge và target evidence | Bundle/TRANSFER/consumer ACK cho G2; authentic same-state pair/ACK cho G3 | Evidence thật đúng consumer, rights, authority và scope; independent gate review | Chưa đạt |
| Luồng tích hợp hữu hạn | Profile/budget, frozen R4a, raw attempt, R4b, gate đúng scope | G1/G2/G3 và prerequisite từng nhánh theo W4 readiness | W4 NOT_RUN_BLOCKED |

Budget của lượt tài liệu này: tối đa 2 vòng sửa sau tự review, 0 fixture/provider/target/training calls. Kiểm read/hash/navigation/preservation và Git publication được thực hiện theo task; đây không phải budget cho runtime sau này.

## Báo cáo và bàn giao

[Progress](progress.md) ghi trạng thái artifact, review, gap và next task. Artifact mới sau review có digest/revision mới; inventory hiện hành ghi hash tài liệu, không cấp admission. Clone public thiếu raw/local reports giữ là LOCAL_ONLY theo source map.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Task tài liệu này không nâng gate. Dự kiến tiếp theo là một consumer packet hoàn chỉnh; chưa dispatch hoặc tạo ACK thay consumer.

## Điều chỉnh theo chỉ thị tiếp theo của người dùng

[Policy knowledge revision 2](../../knowledge/knowledge-policy-v2.md) là hướng dẫn hiện hành về tiếp nhận kiến thức trung lập. DAN và chủ đề tương tự không bị loại khỏi phạm vi nghiên cứu theo nhãn; D01–D11 cũ giữ lịch sử, quyền thực thi và support của claim được xét riêng. REA–IDA được bảo toàn qua các vòng.
