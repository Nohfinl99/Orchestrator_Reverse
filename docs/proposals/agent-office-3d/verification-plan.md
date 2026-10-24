# Kế hoạch kiểm chứng offline

**Mục đích:** chứng minh ý tưởng về màn hình, trạng thái và luồng cuộc họp trước khi nối runtime thật. Các tiêu chí dưới đây là acceptance **đề xuất cho prototype**, chưa được phê duyệt thành gate project. Chưa có UI hoặc kiểm tra behavioral nào được chạy trong lượt lập hồ sơ này.

## Các mốc

| Mốc | Output | Acceptance đề xuất | Status |
|---|---|---|---|
| V0 — scenario & event contract | Schema versioned và event log giả lập | Mỗi event có provenance, IDs và nhãn `SIMULATED`; định nghĩa rõ work/location/presence. | `DESIGN_ONLY` |
| V1 — offline office board | Web scene 3D, timeline và detail panels đọc event log local | Sáu identity hiện có được hiển thị; replay/pause/step; status, location và presence không nhập nhằng; bấm agent xem command, claims, evidence refs, objection và minutes. Không network/model call. | `NOT_IMPLEMENTED` |
| V2 — resilience replay | Deterministic reducer + edge-case event logs | Cùng log cho cùng state; duplicate không lặp action; out-of-order/gap không ghi đè state mới hơn; heartbeat mất hiện stale/offline; unknown event không thành success. | `NOT_RUN` |
| V3 — read-only live bridge | Adapter từ một nguồn agent có scope và quyền | Chỉ sau khi có producer/caller và event binding được chấp nhận; UI gắn event/session IDs và timeline; p95 event-to-render mục tiêu dưới 1 giây là ngưỡng đề xuất, cần owner chấp thuận và đo. | `BLOCKED / FUTURE` |
| V4 — command/control | Orchestrator nhận lệnh, tạo task/meeting, event receipt và điều khiển session thật | Lệnh hợp lệ có receipt; lệnh thiếu quyền/scope/budget không chạy; UI phản ánh refusals/cancel/fail; quyết định chỉ cập nhật DAG theo gate/acceptance. | `SEPARATE_RUNTIME_PHASE` |

## Kịch bản V1/V2

| Case | Event/replay cần có | Kết quả đúng để nhìn thấy |
|---|---|---|
| Lệnh điều phối | Lệnh người dùng → goal/agenda → routing → assign/invite | Lệnh và meeting/task ID hiện trong timeline; hiện lý do route và người nhận; avatar chỉ di chuyển khi có receipt accept/join. |
| Song song | Agent A `working` ở bàn; Agent B `idle`/`available` | A vẫn làm task; B không bị gắn việc do animation. |
| Mời agent bận | Agent A đang `working`, nhận invite | A ở bàn; invite `deferred` hoặc `waiting`; task không biến mất. |
| Họp có tham dự | Invite → accept → joined → contribution | Chỉ người đã accept/join vào phòng; từng ghế gắn agent/meeting ID. |
| Phản biện | Claim X và objection trỏ về event/claim X | Bấm claim thấy căn cứ và phản biện; đường nối/nhãn không thay đổi nội dung gốc. |
| Không đồng thuận | Hai claim mâu thuẫn, synthesis không giải quyết | Hiện hai phương án, tác giả, evidence và câu hỏi mở; không hiện “consensus”. |
| Tổng hợp | Contribution → synthesis → decision candidate | Minutes chỉ dựa contribution đã lưu; decision/action gắn owner và acceptance. |
| Lỗi agent | Timeout, từ chối hoặc lỗi A2A | Lượt đó `failed/declined`; không bịa câu trả lời; meeting có thể tiếp tục hoặc dừng theo rule. |
| Hủy họp | Meeting cancelled khi đang ở lượt N | Lưu trạng thái hủy/lượt cuối; không đánh dấu complete; nhân vật trở về sau event. |
| Mất feed | Heartbeat hết hạn, reconnect, gap | Agent `stale/disconnected`; timeline đánh dấu gap; replay/resync không tạo lệnh giả. |
| Event trùng/sai thứ tự | Duplicate ID; event sequence lùi | Deduplicate hoặc giữ conflict; không đảo trạng thái/animation về state cũ. |

## Bộ công cụ đề xuất

- **3D:** Three.js hoặc React Three Fiber; chọn một sau prototype spike nhỏ, giữ layer model/room tách khỏi event reducer.
- **Event data:** TypeScript types + JSON Schema/Ajv; versioned JSONL fixtures cho offline replay.
- **State/replay:** reducer thuần với clock giả; lưu fixture dùng để tái hiện scenario. Chưa cần model/API hoặc backend để chứng minh V1.
- **UI interaction:** Playwright cho click avatar, transcript, evidence refs, filters, pause/step/replay và màn hình lỗi.
- **Logic:** Vitest cho trạng thái, duplicate/gap/reorder, cancellation và synthesis display; chỉ viết/chạy khi có task implementation được giao.
- **Live transport về sau:** SSE phù hợp feed một chiều; WebSocket nếu cần hai chiều. Lệnh điều phối phải đi qua Orchestrator/broker riêng, không gửi trực tiếp từ animation scene đến agent.
- **Capture/telemetry:** đo thời điểm event nhận và frame cập nhật; lưu event ID/sequence/latency, không cần chain-of-thought.

Các công cụ này là đề xuất, không được cài hoặc chạy trong lượt lập hồ sơ. Việc kiểm IA sẽ chỉ xác minh đường dẫn, manifest và links; không thay các acceptance V1–V4.

