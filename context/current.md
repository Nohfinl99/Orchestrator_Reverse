# Context hiện tại — snapshot 21/10/2026

Orchestrator_Reverse xây lớp điều phối reverse engineering theo goal, task DAG, identity hiện hữu, evidence và gate. REA sở hữu workflow/evidence/ledger; IDA sở hữu native/decompiler/IDB state. Xem [nguyên lý gốc](../CONTEXT_VI.md).

**Lượt công việc gần nhất:** đã trích xuất [12 knowledge card cho điều phối](../docs/knowledge/README.md) từ ba nguồn GitHub, có source pins, WHAT/WHY/HOW, retrieval và giới hạn; đây là candidate reference, chưa admitted KB/ACK. [W4 readiness/gap register](../docs/planning/w4-readiness-plan.md) giữ runtime `NOT_RUN_BLOCKED`; I01–I04 không eligible ở run44, I05 chỉ verified non-target preparation. Nhánh nghiệp vụ tiếp theo vẫn là proposal consumer, chưa dispatch. Prompt/protocol chưa nối loader/runtime.

| Đã có | Giới hạn cần giữ |
|---|---|
| Mười stack và mười protocol offline | Hoàn thành tài liệu không phải hoàn thành W0–W7 hoặc 57 task cũ |
| Mapping sáu role và một projection consumer Triage | Chưa đồng bộ toàn hệ; Stage1 thực tế còn parse trực tiếp |
| Báo cáo logic và verifier custody v2 trong hồ sơ local | Verifier không chứng minh hành vi agent hoặc runtime |
| P1J bounded implementation, lịch sử 53/53 fixture | Kết quả hữu hạn trước IA, không phải test mới hoặc nghiệm thu toàn hệ |
| Navigation IA và chỉ dẫn bàn giao | Chỉ giúp tìm đúng nguồn, không tạo quyền/receipt/ACK |

## Gate kế thừa

| Gate | Trạng thái |
|---|---|
| P1K B4 | FAIL |
| G1 | INCOMPLETE |
| G2 | INCOMPLETE |
| G3 | NOT_RUN |
| G4 | NOT_RUN |
| W4 runtime | NOT_RUN_BLOCKED |
| v3 | OFF |

Nguồn: [validation snapshot gốc](../docs/reference/validation-status.md); locator report local được nêu trong [source map](../docs/reference/source-map.md). [project-state.json](project-state.json) là biểu diễn máy đọc của view này, không phải state machine thực thi. Chưa tái xác minh active REA/IDA session trong task IA.

## Việc tiếp theo

Đề xuất mới nhất là hoàn thiện packet cho **một consumer/call site cụ thể**, giữ `PROPOSED_NOT_DISPATCHED` đến khi có đủ input path/digest/revision, output, budget và acceptance. Selected-consumer projection đã có; không lập lại task như chưa làm. B4 correction là nhánh riêng trước implementation phụ thuộc.

Đọc [work queue](../docs/planning/work-queue.md) để chọn nhánh. Task IA hiện tại không tự dispatch các nhánh này. Các quyết định target/model/provider/numeric runtime budget và quyền pilot chưa được chọn thay người dùng.

## Khi đổi phiên

Đọc [handoff](handoff.md), kiểm scope và revision theo [source map](../docs/reference/source-map.md), rồi chỉ nạp stack/protocol cần thiết. Không lấy README lịch sử hoặc mtime làm bằng chứng trạng thái mới. Nếu chỉ có clone public, các report local chưa có được giữ là `LOCAL_ONLY`, không coi là đã đọc hay xác thực.
