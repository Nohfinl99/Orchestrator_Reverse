# Thư viện skill Orchestrator

Năm workflow của Orchestrator được lưu để gọi lại qua nhiều phiên trong cùng môi trường. Bản chuẩn public nằm trong [`plugins/orchestrator-toolkit/skills/`](../../plugins/orchestrator-toolkit/README.md); bản cài local của workspace nằm trong `.agents/skills/` ở root workspace. Năm thư mục tương ứng là `orch-cua`, `orch-strix`, `orch-d810-ng`, `orch-microsmt` và `orch-ollvm-research`.

## Gọi skill

Đọc [bảng chọn và cách gọi](../../plugins/orchestrator-toolkit/README.md), hoặc mở `SKILL.md` tương ứng trực tiếp. Trong workspace này, bản local đã sẵn và không cần cài lại plugin cho mỗi phiên. Host có hỗ trợ cú pháp gọi tên có thể dùng `$orch-cua`, `$orch-strix`, `$orch-d810-ng`, `$orch-microsmt` hoặc `$orch-ollvm-research`; nếu không, yêu cầu tự nhiên hoặc đọc hướng dẫn theo đường dẫn.

Agent trong public clone cũng có thể đọc `SKILL.md` trực tiếp theo [AGENTS.md](../../AGENTS.md), không cần plugin import. Máy/tài khoản khác cần source access và thiết lập discovery tương ứng. Catalogue/discovery chỉ làm hướng dẫn dễ tìm; quyền truy cập tool, runtime và prerequisite workflow phải được xác nhận riêng.

## Nguồn và phạm vi

- `Orchestrator_Reverse/plugins/orchestrator-toolkit/skills/<name>/SKILL.md` là nguồn public chuẩn để bảo trì.
- `.agents/skills/<name>/SKILL.md` là bản cài local bền qua các phiên của workspace này; khi cập nhật nguồn, đồng bộ bản local có kiểm soát.
- Gói chỉ gồm năm skill nêu trên, không hàm ý toàn bộ host plugin/tool catalogue đã được cài hoặc kết nối.
- Các workflow là hướng dẫn; chúng không đổi sáu identity, REA–IDA, phase/gate, lịch sử FAIL hay prerequisite runtime của dự án.
