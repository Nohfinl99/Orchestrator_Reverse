# Bàn giao và tiếp tục phiên

Đọc [current.md](current.md) để biết trạng thái, [work queue](../docs/planning/work-queue.md) để biết nhánh tiếp theo và [source map](../docs/reference/source-map.md) để mở đúng nguồn. Trang này quy định cách ghi bàn giao ở lớp tài liệu; không thay schema checkpoint/handoff của runtime.

## Đã bàn giao từ lượt IA

- Entry cho AI, context ngắn, bản đồ phase/role/nguồn và thứ tự đọc theo task.
- Ba tài liệu chủ đề được chuyển nguyên byte sang thư mục đích; đường dẫn cũ vẫn dẫn tới bản mới.
- Stack/protocol, nguyên lý, gates, source code và evidence gốc được giữ theo preservation/custody checks.
- Gap về worksheet local, consumer admission, B4 và integration được ghi cụ thể, không giải quyết bằng đổi tên folder.

Xem [bản ghi thay đổi IA](../docs/changes/2026-10-21-information-architecture.md) để biết phạm vi kiểm tra. Tình trạng xuất bản kiểm bằng Git commit/remote hiện có; không suy từ nội dung một checklist lịch sử.

**Bổ sung W4 ngày 21/10/2026:** đọc [readiness/gap register](../docs/planning/w4-readiness-plan.md). Run42 là W4 plan offline; I05 run43 là non-target preparation; run44 reconcile runtime blocked. I01–I04 chưa đủ điều kiện. Gate G4 aggregate `NOT_RUN`, W4 readiness `NOT_RUN_BLOCKED`; cả hai chưa PASS. Hai concern state là finding tĩnh. Không dispatch template hoặc sửa source trong lượt tổ chức này.

## Mẫu ghi cuối phiên

Ghi record mới trong thư mục công việc được task cho phép; report đã freeze dùng revision mới. Khi được phép công khai một record bàn giao, đặt trong `docs/changes/` theo ngày và chủ đề. Không đặt raw/target/private-data vào đây.

```text
Objective và phạm vi đã được giao:
Nguồn đã đọc: path / revision / digest hoặc locator; phần chưa truy cập:
Artifact đã tạo/thay đổi và revision:
Đã hoàn thành trong phạm vi:
Thiết kế / code / execution / review: ghi riêng, chưa chạy ghi NOT_RUN
Kiểm tra đã chạy: command / kết quả / receipt; giới hạn kết luận:
Gate giữ nguyên hoặc thay đổi có exact evidence:
Vấn đề chưa rõ, dependency và điều kiện mở lại:
Một next atomic task đề xuất: owner / input / output / acceptance / budget
Trạng thái proposal hoặc dispatch và quyền tương ứng:
Git commit / branch / remote nếu có:
```

Trước resume: kiểm nguồn có drift, context/IDB revisions và các consumer ACK liên quan theo contract gốc. View IA không tự chuyển task sang READY. Thiếu nguồn chỉ chặn claim/nhánh phụ thuộc; tiếp tục phần độc lập đúng scope.
