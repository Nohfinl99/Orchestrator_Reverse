# Packet offline — INPUT_SUPPORT_PREPARATION_20261024_01

Revision 1; status PREPARED_OFFLINE / CRITERIA_DECISION_PENDING. Producer: phiên Codex hiện tại; independent reviewer chưa được bố trí. Không khai consumer invocation hoặc ACK.

## Objective và input

Xác định các boundary viết lại input/handoff và nguồn knowledge hiện có, lập benchmark đọc nguồn có ground truth để hỗ trợ các task hợp lệ bị hiểu sai hoặc thiếu context. Phân biệt packet integrity reject, model refusal, tool/client-policy error, provider unavailable, capability gap và material ambiguity. Chưa có raw model-refusal sample trong nhánh mới; false-refusal rate hiện chưa đo được.

Người dùng đã chọn packet offline và cho phép lựa chọn benchmark có bằng chứng thật. Người dùng giao chọn model phù hợp độ khó cho bước sau. Model ID, provider, dữ liệu được upload và numeric invocation budget chưa bind; không mở calls từ packet này.

Selected consumer để source-map: `archive/RE-Decom/01_control_plane/prompt_master.py:430–433`, `PromptMaster.build_full_agent_prompt(role, task_message)`. Đây là archived builder được chọn cho proposal, không khẳng định là active model dispatch. `craft_rtccoe_prompt` giữ raw_user_prompt ở dòng 534. Ledger handoff có sanitizer là boundary khác; không âm thầm nối sanitizer vào user input hoặc gọi nó trong lượt chuẩn bị.

Source pins ở workspace `evidence/orchestrator_meetings/20261024_input_support_gates_01/source-pins.json` (LOCAL_ONLY). Baseline public là commit `82242c9f492fc20b636fb7504ade0fb4409962cb`; source archive/candidate có digest riêng, không lấy commit public làm revision giả cho archive.

## Output, budget và stop

- Public: proposal, packet, benchmark plan và status worksheet có nguồn/giới hạn.
- Local: transcript quyết định được chép từ hội thoại có provenance, capability metadata snapshot, source pins, receipt kiểm captures/benchmark raw và báo cáo. Transcript chép lại không phải bản ghi byte-authenticated từ API hội thoại.
- Budget chuẩn bị: tối đa 6 seed case tài liệu có nguồn; readback 10 historical tooling case; tối đa 2 vòng sửa tài liệu; 0 model/provider/target/training calls, 0 fixture rerun. Kiểm IA/read/hash và Git publication chỉ cho public package.
- Stop: nguồn mismatch → dừng claim phụ thuộc và giữ expected/actual; thiếu model/example/reviewer/decision → giữ pending; thay đổi API/source archive/identity/rights → proposal riêng.

Acceptance đề xuất: các tiêu chí checklist được anh nhận; source references khớp; không lẫn historical tooling suite với pentest/REA target run; không biến candidate knowledge thành runtime admission; original input/intent/raw evidence không bị thay ngầm. Chưa có independent review hoặc user acceptance của packet này.

## Sau lượt chuẩn bị

Anh quyết định có dùng benchmark đọc nguồn trước dù chưa có model-refusal examples hay không, và chốt checkpoint/threshold. Khi mở model run, pin cụ thể profile/budget/capture và adjudicated oracle; applicable R4a review/freeze trước execution. Nếu chọn native artifact/static REA, chốt artifact/action/source ownership và prerequisite G3/pair của nhánh; code repository analysis tiếp tục dùng source tools bình thường.
