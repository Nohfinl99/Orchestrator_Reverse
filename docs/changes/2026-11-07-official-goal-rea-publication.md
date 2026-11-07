# Điều chỉnh chính thức goal continuity và áp dụng REA

Ngày 07/11/2026. Bản này đưa các thay đổi đã review trong workspace vào gói public có source/test và entry dùng được sau clone. Không thay sáu identity, REA–IDA contract, phase/gate hoặc lịch sử FAIL.

## Hành vi điều phối

- [Goal continuity](../operations/goal-continuity.md): giữ original và user revisions, xác định active goal, map branch/criterion; refusal/blocker không cấp quyền tự đổi outcome. User chọn nhánh phụ khác với rút/thay original; lời làm rõ mới rõ nghĩa có hiệu lực mà không cần câu mẫu.
- [Áp dụng REA](../operations/rea-application.md): toolkit phân tích MCP/CLI và provider IDA khác pair contract project. Chọn route theo artifact/câu hỏi thật, preserve Evidence và giới hạn; bundle/snapshot/live IDB không thay thế lẫn nhau.
- README, AGENTS, GEMINI và workflow thao tác dẫn trực tiếp các hướng dẫn này. Review cuối phải nói scope của acceptance, phần chưa làm và nguồn quyết định.

## Source local được đưa cùng

[Session controller](../operations/local-session-controller.md) và [loop guard](../operations/local-loop-guard.md) là phần phụ thuộc đã có review local trước đó, nay có trong gói public: `orchestrator_session/`, `scripts/session_task.py`, `scripts/loop_guard.py` và tests. Controller v1 giữ original/request bytes, task/attempt/source/output bindings; guard opt-in giữ lineage, budget và progress evidence. `check/report` hiển thị `goal_review` để so original với objective/scope/criteria do caller khai; alignment chưa verify và original resolution NOT_ESTABLISHED.

Đây là file-only helpers. Không gọi agent/model/tool/provider, xác thực reviewer/user decision hoặc tự hoàn tất semantic acceptance. Existing input-preparation CLI và persisted session v1 contracts giữ nguyên. Guard chưa là scheduler/global enforcement; dùng v1 trực tiếp không đi qua guard.

## Kiểm và giới hạn xuất bản

CI hiện kiểm inventory/preservation/navigation và synthetic local unit contracts. Các unit tests dùng text/files tạm trong scope local; không chạy binary, provider, ngân hàng, business fixture, training hoặc W4. Raw review/pilot/replay nằm workspace cha, LOCAL_ONLY_NOT_DISTRIBUTED; public chỉ có source/test, guides và summary có phạm vi.

Các kết quả hữu hạn và giới hạn lịch sử giữ ở [delta goal continuity](2026-11-06-goal-continuity.md), [controller](2026-11-01-local-session-controller.md), [loop guard](2026-11-01-local-loop-guard.md). Publication không biến chúng thành benchmark model, REA–IDA pair/ACK hoặc giảm refusal đã đo. Không đưa archive/raw/chat/target/IDB/config vào repository public.

Giữ P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Host dispatch, semantic enforcement và actual caller-bound pilot vẫn chưa hoàn tất.
