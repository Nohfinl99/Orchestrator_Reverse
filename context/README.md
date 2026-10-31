# Context: hiện hành và lịch sử

| Cần gì | File |
|---|---|
| Trạng thái và chọn nhánh tiếp tục | [current.md](current.md) |
| Bàn giao/revalidation trước resume | [handoff.md](handoff.md) |
| View gate toàn hệ | [project-state.json](project-state.json); không là state machine thực thi |
| State của leaf CLI offline | [local-pipeline-state.json](local-pipeline-state.json) |
| State direct IDA acquisition local | [native-local-state.json](native-local-state.json) |
| Chronology current trước rút gọn | [current-history-2026-10-24.md](current-history-2026-10-24.md) |
| Chronology handoff trước rút gọn | [handoff-history-2026-10-24.md](handoff-history-2026-10-24.md) |

Hai history file giữ nguyên bytes của entry được capture ngày 31/10, có nội dung qua 24/10. Chúng ở cùng thư mục để các link tương đối cũ còn hợp lệ. Chỉ mở khi cần lịch sử; không nạp cùng current/handoff theo mặc định. Manifest lịch sử vẫn bind exact revision gốc của nó, không tự được repin sang các bản copy này.

Trạng thái leaf, proposal và global gates là các scope khác nhau. Khi mâu thuẫn, theo nguồn/revision/dependency trong [source map](../docs/reference/source-map.md), giữ conflict và [vấn đề mở](../docs/reference/open-questions.md); không chọn theo tên/ngày sửa file.
