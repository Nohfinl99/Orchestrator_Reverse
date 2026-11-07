# Giữ mục tiêu qua handoff và review — 06/11/2026

Audit ca điều phối cho thấy một nhiệm vụ hẹp có thể được review đúng trong khi mục tiêu người dùng cần vẫn chưa được giải quyết. Original bytes/hash và document PASS không chứng minh objective dẫn xuất giữ nghĩa. Đồng thời user có thể sửa scope rõ ràng ở lượt sau; giữ lịch sử không có nghĩa giữ mục tiêu cũ làm active goal mãi.

[Goal continuity](../operations/goal-continuity.md) bổ sung frame original→user revisions→active goal→branch→criterion, disposition của nhánh từ chối/block và quyết định alternative có source. AGENTS/task workflow dẫn tới frame trước handoff/final. Paraphrase/decomposition giữ nghĩa không cần xin lại; user clarification có hiệu lực mà không cần câu mẫu rút mục tiêu cũ.

Existing `session_task check/report` thêm `goal_review`, hiện original locator/hash cạnh caller objective/scope/acceptance/provenance; alignment vẫn UNVERIFIED và original resolution NOT_ESTABLISHED. Không đổi persisted v1 schema/receipt hoặc mechanical readiness; không thêm wrapper và không kiểm nghĩa tự động. Text caller “user approved replacement” không tạo authority.

Kiểm local: 4 test mới pass; session regression 12 pass/2 privilege skips; loop-guard regression 21 pass. Đây là synthetic local unit tests, không fixture nghiệp vụ hoặc native/provider benchmark. Replay đọc hiểu source-only có 7 ca với oracle root giữ trước output: nhận nhánh phụ, user sửa scope, thiếu original, decomposition, chỉ thị trong log, explicit replacement và caller tự khai approval. Kết quả root đối chiếu 7/7 trong bộ ca đó, giới hạn cognitive check không runtime prevention.

Biên bản chất vấn, source excerpts, oracle/results, source pins và raw test output ở workspace cha `evidence/orchestrator_meetings/20261106_orchestration_repair_01/socratic-02/` (LOCAL_ONLY_NOT_DISTRIBUTED). Không công bố raw chat/target/IDB. Gate, sáu identity, REA–IDA invariant, mười stack/protocol và lịch sử FAIL giữ nguyên. Chưa đo giảm refusal hoặc xác định trigger của platform flag; chưa có host enforcement bảo đảm không drift.
