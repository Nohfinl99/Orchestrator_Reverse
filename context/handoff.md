# Bàn giao ngắn và tiếp tục theo task

Đọc [current](current.md), chọn một objective/caller/output và đúng [cognitive task](../docs/proposals/cognitive-routing/README.md). Tra [source map](../docs/reference/source-map.md) để mở exact revision; chỉ nạp protocol/skill cần dùng.

Ngày 31/10 đã tạo guide chọn CT/owner/model, thiết kế Paperclip projection/outbox và reference Cloudflare chọn lọc. Graph/source manifest và CLI truy xuất giới hạn là LOCAL_ONLY ở workspace cha: `knowledge_graph/`, `scripts/query_knowledge.py`. Biên bản/review local: `evidence/orchestrator_meetings/20261031_context_sync_01/`. Đây là docs/navigation tooling, chưa active loader/Paperclip sync/KB admission hoặc benchmark model. Không tự dispatch proposal từ biên bản.

Trước resume, kiểm input/source/context/dependency/IDB revisions và consumer ACK áp dụng. Digest mismatch thì giữ expected/actual và reject binding đó. Upstream đổi thì revalidate/invalidate downstream, tạo revision mới; receipt còn hợp lệ được reuse sau revalidation theo contract. Không giả issuer/approval từ caller flag, graph hoặc comment.

Native local và CLI có scope/receipt lịch sử riêng trong [current](current.md); không rerun hoặc suy W4 PASS. B4 correction, product-dependent pilot, bridge/provider và isolation/harness cần task/prerequisites riêng. Owner/nguồn/gate chưa đủ thì chỉ chặn nhánh phụ thuộc.

Mỗi bàn giao ghi:

- Objective/scope, owner/reviewer và model thực tế.
- Input path/revision/digest, range đã đọc và phần mới kiểm kê.
- Artifact/output digest/revision; design/code/execution/review tách riêng.
- Check đã chạy và giới hạn; chưa chạy ghi NOT_RUN.
- Gate giữ nguyên hay có exact evidence thay đổi; conflict/unknown không xóa.
- Delta tiến triển, budget còn, stop/reopen condition và một next task đề xuất.

Cùng failure signature mà không có delta evidence thì STOP; tối đa hai vòng document review trong task/candidate, không tự reset bằng finding mới. Runtime cap phải có numeric budget riêng. REA–IDA, sáu identity, source pins và FAIL được kế thừa.

Giữ P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Không có live provider/target/training hoặc Paperclip API run từ lượt điều hướng này; các phiên agent họp là review sessions thực, không phải sáu role runtime đã deploy.

[Handoff trước khi rút gọn](handoff-history-2026-10-24.md) và [current lịch sử](current-history-2026-10-24.md) được lưu nguyên byte ngày 31/10, chứa chronology qua 24/10. Manifest lịch sử giữ nguyên binding của revision gốc, không repin sang bản mới. Public clone không mang archive/raw/evidence/graph workspace cha.
