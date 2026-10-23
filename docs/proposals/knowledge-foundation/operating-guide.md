# Làm việc từ một yêu cầu đến bàn giao

Hướng dẫn thao tác này dùng [protocol hiện hữu](../../../prompt_stacks/README.md); [worksheet](packet-template.md) giúp soạn hồ sơ, không là schema/API runtime mới.

## Bắt đầu bằng một objective

Đọc context và source-map, chốt câu hỏi cần giải quyết và artifact phải bàn giao. Phân loại theo công việc thực: tài liệu ngoài target, knowledge transfer, target analysis hoặc integration. Với chuẩn bị ngoài target dùng NON_TARGET_PREPARATION, pair=null, NOT_RUN; không đòi pair giả để có thể viết tài liệu.

Chọn một đầu ra nhỏ. Ví dụ “lập compatibility proposal cho generated-prompt consumer Triage tại một call site” kiểm được hơn “đồng bộ toàn bộ sáu agent”. Stage1 parser hiện được projection local mô tả không tự trở thành LLM consumer do thay prompt.

## Chọn context và lập DAG

Ghi từng input path/revision/digest, đã đọc phần nào, quyền dùng và giới hạn. Chọn card đúng objective bằng [retrieval guide](../../knowledge/prompt-orchestration/retrieval-guide.md); ghi cả phần không chọn. Link discovery chưa mở giữ DISCOVERY_ONLY. Unknown rights giữ catalog-only theo knowledge protocol.

Prompt-Master lập dependency trước chọn owner. Triage-Sentinel làm reconnaissance; Decomp-Analyst dùng triage evidence để phân tích sâu; Crypto-Logic-Specialist chỉ được xét khi evidence thuật toán phù hợp. Evidence-Synthesizer kiểm support/conflict; Product-Evolution-Architect làm proposal sản phẩm khi objective và accepted evidence phù hợp. HITL giữ approval/execution được cấp. Các nhánh này theo task, không là pipeline bắt buộc có đủ sáu role.

## Xét điều kiện trước bàn giao

| Kiểm | Câu hỏi | Khi chưa đạt |
|---|---|---|
| Integrity | Exact source/input có khớp pin? | Reject binding mismatch, giữ expected/actual |
| Context/applicability | Task/action này thực sự cần pair/knowledge/gate nào theo policy? | Unknown giữ chờ/review, không tự miễn bằng flag |
| Authority/capability | Actor/action/scope có quyền và tool thật? | Chờ quyền hoặc blocked theo contract |
| Knowledge | Source/rights/admission và ACK có bind bundle/context/review revision? | Chặn nhánh tiêu thụ knowledge phụ thuộc |
| Target pair | REA–IDA có cùng target/component/slice/IDB state và receipt fresh/applicable? | Chặn target consumption/completion; acquisition được cấp quyền riêng có đường bootstrap |
| Dependency/budget | Upstream/gates và numeric budget/stop đã rõ? | Chặn đúng nhánh thiếu prerequisite |

Status phải có issuer/validator và receipt phù hợp, không chỉ là chuỗi caller gửi. Candidate local có predicate chưa đồng nghĩa broker hoặc validator thật đã được nối. Prompt trust label cũng chưa chứng minh isolation runtime.

## Bàn giao và kiểm kết quả

Consumer kiểm output, source/context/dependency revisions và applicability rồi mới ACK cho chính scope của mình. Knowledge ACK, target pair ACK, custody check và action authority là bốn việc riêng. Receipt hợp lệ có thể reuse sau revalidation; IDB/source/dependency đổi thì invalidate hoặc revalidate downstream evidence/ACK theo contract.

Record giữ source fact, inference, hypothesis, conflict và unknown. Ghi decision facts/locator; không yêu cầu private reasoning. Khi evidence đầy đủ mà mâu thuẫn, chuyển review và giữ cả hai phía. Reviewer độc lập phải khác producer/executor trong scope applicable; chưa có reviewer thật thì ghi chưa review.

## Sửa và xuất bản

Sửa tài liệu navigation: review diff, cập nhật inventory có chủ đích và chạy verifier IA. Sửa integration: chọn một source/caller và compatibility scope; B4 correction riêng trước implementation phụ thuộc; R4a được review/freeze trước fixture, raw sau attempt, R4b độc lập rồi mới xét acceptance. Retry cần revision/attempt mới, budget còn và bằng chứng tiến triển.

Public chỉ lấy nội dung root Orchestrator_Reverse. Report local dùng locator LOCAL_ONLY hoặc bản tóm tắt public đã review; không tạo link thoát root. Chuẩn bị diff và publication branch cụ thể, giữ attribution và frozen pins. Handoff ghi artifact/revision, tiến độ, check đã chạy, gap và next action; không suy runtime PASS từ verifier tài liệu.
