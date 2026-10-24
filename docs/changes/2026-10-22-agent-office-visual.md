# Review hình ảnh và đề xuất khởi động prototype — 22/10/2026

## Objective

Điều phối review hướng hình ảnh cho văn phòng agent, chọn một concept có ý nghĩa vận hành và đề xuất bước bắt đầu dự án thật dựa trên roadmap/preflight.

## Thay đổi

- Thêm `docs/proposals/agent-office-3d/visual-review-2026-10-22-01.md` với visual direction “phòng quan sát điều phối”, motion/state semantics, fallback, scope visual MVP và no-go.
- Cập nhật roadmap AO-2, profile index, work queue, navigation và handoff.
- Khuyến nghị `START AO-1 NOW` (packet, scenario, event contract, fixture/oracle, acceptance); AO-2 offline UI chỉ sau AO-1 review/acceptance. Không bắt đầu runtime integration.
- Concept frame được tạo để xem hướng layout/mood; ảnh và số liệu minh họa không được dùng làm source, acceptance hoặc product data.
- Advisory reviewers: product visual direction và feasibility/code readiness. Không sửa code, không dispatch, không chạy benchmark/tests.

## Nguồn đã đọc

- `START_HERE.md`, `Orchestrator_Reverse/AGENTS.md`, office profile/roadmap/preflight/runbook.
- `src/README.md` và `src/candidates/README.md`: ba prototype offline riêng; role router `PREPARED_NOT_DISPATCHED`, `dispatch_status=NOT_IMPLEMENTED`; không có app office implementation trong package hiện hành.

## Kiểm tra

IA verifier chỉ kiểm tài liệu/navigation sau khi cập nhật. Không chạy UI, benchmark, fixture, provider, target hoặc runtime.
