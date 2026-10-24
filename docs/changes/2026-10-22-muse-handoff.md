# Xuất bản nhánh và bàn giao Muse — 22/10/2026

## Objective và phạm vi

Người dùng yêu cầu push dự án lên một nhánh GitHub, gửi hướng dẫn Muse tiếp quản và giải thích cách Prompt-Master bàn giao kiến thức. Phạm vi xuất bản là repository public `Orchestrator_Reverse`, remote `https://github.com/Nohfinl99/Orchestrator_Reverse.git`, nhánh `codex/agent-office-3d-muse-handoff`. Workspace cha, archive/raw, source local và config riêng không thuộc gói.

## Đầu ra

- [Điểm tiếp quản Muse](../onboarding/muse-takeover-2026-10-22.md): trạng thái, artifact hiện có, đường tiếp tục, gap, Prompt-Master WHAT/WHY/HOW, receipt do người nhận tự ghi và prompt copyable.
- [Manifest chuyển tài liệu](../../metadata/muse-knowledge-transfer-2026-10-22.json): exact byte digests, selected/rejected, phân biệt background với evaluation reference; `consumer_ack=NOT_RECEIVED`, `kb_admission=NOT_ADMITTED`.
- Giữ các AO-1 revision/review trước và pentest candidate trong lịch sử. Ghi `AO-HANDOFF-01` thay vì sửa bytes reviewed candidate6 để che câu review-state mâu thuẫn.
- Cập nhật entry, navigation và content inventory. Không đổi preservation pins, mười stack/protocol, identity hoặc gate.
- `.gitattributes` giữ nguyên bytes của cây proposal office khi Git xuất bản; tránh tự đổi CRLF/LF làm lệch digest fixture/review đã soạn. Đây là bảo toàn byte, không phải sửa hay repin candidate. Các blank lines cuối file lịch sử được giữ.

## Review và kiểm tra

Publication-scope review đọc các file thay đổi trong gói public; không phát hiện credential-like value, private/raw/config addition hoặc real attack endpoint. Reviewer yêu cầu refresh content inventory và ghi rõ mâu thuẫn v6; các việc này được đưa vào lượt xuất bản. Handoff được review riêng trước commit.

Kiểm IA trước push dùng `scripts/verify_ia.py` cho navigation/digest/preservation. Kết quả lệnh thực tế được báo cùng commit cuối phiên; bản ghi này không tạo execution receipt hay R4a/R4b. Không schema-validate, replay hoặc benchmark fixture. Không chạy target/provider/runtime.

Git commit cuối cùng được Git xác định sau khi commit; không chèn SHA tự tham chiếu vào manifest. Người nhận bind exact checkout HEAD và SHA-256 manifest của chính clone họ nhận. Push branch không mở AO-2 hay đổi acceptance của candidate.

Giữ P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`.
