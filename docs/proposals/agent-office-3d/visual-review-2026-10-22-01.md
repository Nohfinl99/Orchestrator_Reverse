# Review hình ảnh và đề xuất khởi động prototype thật

| Trường | Giá trị |
|---|---|
| Review ID | `AGENT_OFFICE_VISUAL_REVIEW_20261022_01` |
| Input | Roadmap AO-0…AO-7, preflight package, source review |
| Type | `VISUAL_DESIGN_REVIEW / ADVISORY` |
| Result | `RECOMMEND_START_AO1_NOW / AO2_AFTER_AO1_ACCEPTANCE` |
| Execution | `NO_UI_IMPLEMENTATION / NO_RUNTIME_DISPATCH` |

## Câu hỏi

Hình ảnh văn phòng nên thể hiện điều phối kỹ thuật như thế nào để người dùng đọc được lệnh, trạng thái và phản biện mà không nhầm animation với hành động agent thật? Đã đủ căn cứ để bắt đầu làm sản phẩm thật chưa?

## Hướng hình ảnh được chọn

### “Phòng quan sát điều phối”

- Không gian 3D nhỏ, dạng isometric/top-down nhẹ, làm bản đồ trực quan chứ không chiếm hết màn hình.
- Bên cạnh là timeline event cố định và panel meeting/evidence. Timeline/panel là nguồn đọc chính xác; cảnh 3D là cách nhìn nhanh ai đang ở đâu.
- Màu trạng thái đi cùng text/icon: teal cho connected/working, amber cho pending/deferred/stale, red cho blocked/failed, green chỉ cho complete/verified khi event evidence cho phép. Không mã hóa status bằng màu đơn lẻ.
- Luôn hiện `SIMULATED / OFFLINE` trong prototype; trạng thái số liệu trong concept art chỉ là placeholder, không phải metric dự án.
- Chuyển động ngắn theo event: lệnh pending chỉ lên timeline; invited chưa accept không tự đi; accepted/joined mới đi tới ghế; contribution hiện cue người nói; objection liên kết claim; close/return chỉ theo event kết thúc.
- Hỗ trợ chọn agent bằng bàn phím, danh sách/timeline 2D thay thế, reduced-motion mode, zoom/pan và trạng thái stale/unknown có nhãn.

### Vì sao không làm kiểu game office

Game-like office với avatar đi dạo/bong bóng sinh động cho demo hấp dẫn, nhưng dễ khiến trạng thái ngầm hoặc animation trông như bằng chứng. Hướng quan sát điều phối ưu tiên blocker, task, receipt, evidence, dissent và next action. Có thể thêm ambient animation về sau nếu không che hoặc giả lập event.

## Lát cắt visual MVP được đề xuất

Một screen duy nhất, dữ liệu fixture local:

1. Roster đủ sáu identity hiện hữu; scenario chỉ làm chuyển động cho participants có event. Agent bận vẫn ở bàn với badge `DEFERRED`; task gốc tiếp tục là working.
2. Một cụm bàn + một phòng họp nhỏ; hai participant được invite/accept/join theo event. Nhân vật khác đứng yên theo state fixture.
3. Timeline hiển thị command requested → invite/defer/accept → join → contribution → objection → synthesis → close, mỗi dòng có event ID/sequence.
4. Click agent mở task/status/meeting; click claim mở source locator hoặc `NO_EVIDENCE_REF`; click dissent mở objection và claim liên quan.
5. Panel synthesis tách agreements, dissent, open questions và next action. Không tạo consensus khi fixture chứa mâu thuẫn.
6. Pause/step/replay và bảng 2D dự phòng dùng cùng reducer/event source.

## Ý kiến review và phản biện

**Ủng hộ:** visual scene giúp định vị nhanh agent/task/meeting và làm event flow dễ quan sát; scene tối giản + timeline/evidence panel vẫn có thể triển khai thành vertical slice offline.

**Phản biện:** hiện chưa có UI codebase được chọn, AO-1 event/fixture/oracle chưa được chấp thuận; làm AO-2 ngay sẽ xây scene trên semantics chưa đóng. Một mockup đẹp không chứng minh UX tốt, semantic correctness hoặc live dispatch.

**Adjudication:** khởi động dự án thật ở **AO-1 ngay** — chốt scenario, event contract, fixture/oracle, storyboard và acceptance; sau khi AO-1 được review/chấp thuận, bắt đầu AO-2 là visual prototype offline thật. Không khởi động live bridge hay điều khiển agent. Đây là recommendation mở việc, không phải runtime dispatch record.

## Đề xuất quyết định

**GO:** làm AO-1 packet và một spike có phạm vi nhỏ để xác định canvas/scene approach, sau khi scope/owner được ghi trong task packet. Spike chỉ dựng 1 room/desk với sample state offline; chưa tạo full office.

**Sau AO-1:** giao AO-2 UI implementation nếu candidate/schema/oracle được review, acceptance freeze xong, codebase/owner/budget đã chọn và task được người điều phối chấp thuận.

**NO-GO hiện tại:** multi-room office hoàn chỉnh, custom avatar/asset pipeline, agent tự đi tự nói, model/provider call, live integration, command/control.

## Ranh giới claim

- Concept frame do image generation tạo để thảo luận layout/mood; nhãn/trạng thái/số trong ảnh minh họa có thể không chính xác, không dùng làm acceptance/data.
- Reviewer chỉ đưa khuyến nghị hình ảnh/roadmap; không phải sáu identity đã nhận task hoặc ACK.
- Chưa có implementation, test, benchmark hoặc user study; chưa chứng minh 3D vượt 2D.
- Gate gốc giữ nguyên: P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 `NOT_RUN_BLOCKED`; v3 `OFF`.
