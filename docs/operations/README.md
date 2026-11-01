# Điều hành theo tác vụ

[Thư viện skill dùng lại, không cài lại mỗi task](skill-library.md) · [Folder nguồn năm skill](../../plugins/orchestrator-toolkit/README.md).

Đọc [current](../../context/current.md), chọn một mục tiêu và mở đúng nhánh dưới đây. Chỉ nạp protocol/skill phục vụ công việc; không replay toàn bộ lịch sử hoặc gọi đủ sáu role cho mọi task.

| Công việc | Điểm vào | Giới hạn |
|---|---|---|
| Chọn cognitive task, owner và model | [CT guide](../proposals/cognitive-routing/README.md) → [worksheet dùng lại](../proposals/cognitive-routing/task-worksheet.md) | Model cao review chuyên môn; Luna hỗ trợ bounded work. Đây chưa là router runtime |
| Chọn workflow CUA, Strix, D810-ng, MicroSMT hoặc OLLVM research | [Orchestrator Toolkit](../../plugins/orchestrator-toolkit/README.md) → [toolkit use and portability](toolkit.md) | Local exporter kiểm gói; account import, activation và runtime chưa được xác nhận |
| Nhận việc, giao việc và review đầu ra | [Task execution](task-execution.md) | Workflow phiên agent; không chứng minh broker/runtime đã nối |
| Tìm knowledge liên quan | [Knowledge index](../knowledge/README.md) | Chọn source/condition/locator; candidate reference chưa admission/ACK |
| Kết hợp Paperclip | [Sync/outbox spec](../proposals/cognitive-routing/paperclip-sync.md) | Chưa connected; task done không thay evidence/gate/approval |
| Review source security | [Cloudflare selection](../proposals/cognitive-routing/cloudflare.md) | Phương pháp chọn lọc; chưa cài skill hoặc chạy full audit |
| Tiếp tục CLI/native local | [Current theo nhánh](../../context/current.md) → [work queue](../planning/work-queue.md) | Leaf local có scope riêng; không tự rerun hoặc mở W4 |
| Xem kết quả kiểm 31/10 | [Publication và pentest summary](../changes/2026-10-31-context-routing-publication.md) | 47 case của query CLI local, không benchmark model hoặc toàn hệ |

## Thư mục và trách nhiệm

| Nơi | Chứa gì |
|---|---|
| [context](../../context/README.md) | Entry/state hiện hành và bản history được phân biệt rõ |
| `docs/operations/` | Điểm vào thao tác theo objective, không định nghĩa authority mới |
| [docs/proposals/cognitive-routing](../proposals/cognitive-routing/README.md) | Guide/worksheet và các thiết kế integration chưa nối runtime |
| [docs/knowledge](../knowledge/README.md) | Tri thức tham khảo có nguồn, conditions và giới hạn |
| `docs/changes/` | Bản ghi thay đổi/public summary theo revision |
| [prompt_stacks](../../prompt_stacks/README.md) | Mười stack và mười protocol gốc giữ bytes/đường dẫn |
| `metadata/`, `scripts/verify_ia.py` | Inventory/navigation/read-hash checks của gói public |

Graph, query CLI và raw pentest nằm trong workspace local, **LOCAL_ONLY_NOT_DISTRIBUTED**. Public clone chỉ có guide, summary và digest locators, không tự chạy lại được suite này. Không thêm raw/target/IDB/config để lấp gap. Đưa một file vào graph không chứng minh file gốc hết hiệu dụng; lịch sử/FAIL/pins vẫn giữ.

## Luồng PR và merge

Từ `main` đã đồng bộ → nhánh `codex/` cho một objective → review exact diff → inventory và verifier → PR → kiểm tra CI và head SHA → merge. Không gộp nhánh lịch sử chỉ theo tên; kiểm ancestry và nội dung để tránh đưa trạng thái cũ quay lại.

Workflow `Verify public documents` chỉ kiểm integrity/navigation của public package. Không chạy workload, provider hoặc target; CI xanh không là gate PASS. Nếu workflow chưa chạy/không đạt thì giữ pending và xử lý đúng finding; không bỏ qua check hoặc thay protection để merge. Thiết lập required-check/branch protection của server là cấu hình riêng, không được tuyên bố đã bật từ việc có workflow.
