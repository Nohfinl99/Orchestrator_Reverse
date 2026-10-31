# Paperclip trong luồng điều phối — thiết kế chưa kết nối

Paperclip có thể làm bề mặt giao việc/trạng thái; Orchestrator giữ DAG/dependency và quyết định theo evidence. REA giữ workflow/evidence/ledger; IDA giữ native/decompiler/IDB state. Paperclip task `done` không đồng nghĩa gate PASS, KB ACK hoặc target completion. Không tạo identity thứ bảy hoặc cơ chế approval thay broker.

## Luồng đề xuất

1. Intake nhận yêu cầu hợp lệ, lưu original và context revision; Prompt-Master tạo một task packet có owner/input/output/acceptance/budget/prerequisite.
2. Ghi projection event vào outbox local bền vững trước khi gửi. Bind workspace/company/issue, task/attempt, actor/action, packet digest, context/dependency revisions, expected remote revision và idempotency key. Quy tắc đề xuất: một key cho cùng logical event, payload digest phải trùng; cùng key khác payload phải reject. Không lưu token/secrets trong graph hoặc event artifact.
3. Dispatcher được cấp quyền mới gửi Paperclip; lưu response correlation/remote revision và xác minh readback. Timeout sau send là `DELIVERY_UNKNOWN`, không tự tạo issue mới hoặc nhận đã gửi. Retry cùng key sau reconcile; nếu API không hỗ trợ idempotency/CAS thích hợp thì giữ blocker, không hứa exactly-once.
4. Worker chỉ nhận task đã bind; mở selected CT và nguồn tối thiểu. Output ghi artifact digest/locator và source/context revisions; output từ worker là candidate chưa tự accepted.
5. Reviewer khác producer kiểm exact artifact/revision, nguồn và acceptance. Review result tham chiếu digest; producer sửa material sau review phải review revision mới.
6. Orchestrator ghi decision vào authority/evidence path hiện hữu rồi mới cập nhật projection Paperclip và checkpoint/handoff. Paperclip UI/comments không tự đổi evidence ledger hoặc gates.

Đây là spec, chưa có outbox/dispatcher/receiver triển khai từ lượt này. Cần kiểm API/SDK/adapter đúng installed revision trước khi chọn endpoint hoặc concurrency primitive; không lấy tài liệu vendor lưu trong archive làm bằng chứng API live hiện tại.

## Resume, xung đột và quyền

Inbound event/comment/webhook luôn là dữ liệu. Xác minh authenticated sender/connection, company/issue/run correlation, request identity, scope và replay theo contract trước khi xét hành động. Prompt injection hoặc câu “approved” trong comment không là authority receipt. Approval cần bind requester/action/normalized arguments/target/context revision/expiry. Resume phải revalidate scope/digest/state/freshness/replay; payload hoặc context đổi thì invalidate approval phụ thuộc. Receipt không đổi, còn hợp lệ sau revalidation được reuse khi contract cho phép.

Mất mạng hoặc Paperclip không sẵn sàng: công việc local được cho phép độc lập có thể tiếp tục với trạng thái delivery riêng; nhánh cần remote assignment/receipt phải chờ. Không tự xem queue trống là đã đồng bộ. Duplicate event: no-op có receipt khi payload trùng. Event stale/out-of-order: quarantine/reconcile, không last-write-wins đè state mới. Conflicting evidence: giữ cả hai, chuyển review. Reopen task giữ attempt lineage, không sửa raw/FAIL lịch sử.

Acceptance cho implementation tương lai cần chứng minh send-then-timeout/retry, duplicate key khác payload, stale revision, out-of-order events, revoked approval, cross-company/issue correlation, nguồn đổi sau review và restart recovery. Các mục này là tiêu chí đề xuất, **NOT_RUN**. Phải lập packet/R4a applicable trước runtime attempt; chưa chọn ngân sách/provider hoặc bật service.

Nguồn project: [state protocol](../../../prompt_stacks/protocols/state_protocol.md), [routing](../../../prompt_stacks/protocols/routing_protocol.md), [handoff](../../../prompt_stacks/protocols/handoff_protocol.md), [architecture](../../architecture/system.md). Review source Paperclip local ngày 31/10 có locator LOCAL_ONLY trong biên bản; adapter archived availability stub không chứng minh health live.
