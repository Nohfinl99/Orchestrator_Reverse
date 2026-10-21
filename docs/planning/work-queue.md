# Hàng đợi công việc

Đây là view đề xuất từ hồ sơ ngày 21/10/2026, không phải dispatch ledger. Task hiện hành do yêu cầu người dùng quyết định; IA chỉ làm rõ tiến độ và dependency. [Source map](../reference/source-map.md) ghi nguồn local của từng nhánh.

| Nhánh | Đã có | Cần làm tiếp | Điều kiện / owner trách nhiệm |
|---|---|---|---|
| IA | Context, source/phase/role map, navigation và preservation | Bảo trì theo report mới có nguồn | Documentation task; không đổi gates |
| Một consumer cụ thể | Selected Triage projection và proposal `SELECTED_TRIAGE_CONSUMER_ADAPTER_COMPATIBILITY_PROPOSAL_01` | Hoàn thiện input path/digest/revision, một caller/action, output, budget và acceptance; freeze/review packet | PROPOSED_NOT_DISPATCHED; Prompt-Master, Evidence-Synthesizer review riêng |
| P1K B4 | V3 FAIL được giữ; catalog/oracle inconsistency đã mô tả | Correction candidate revision riêng và review exact digest | Trước caller-boundary implementation phụ thuộc; owner contract/oracle hiện hữu |
| Knowledge bundle | Protocol; [12 candidate card từ ba nguồn](../knowledge/README.md), source pins, rights disposition và retrieval guide | Chọn một consumer/objective; review source/applicability, exact bundle/context binding, TRANSFER và ACK thật; S1 chỉ catalog metadata | G2 chưa đóng; candidate chưa admitted, chưa independent review/ACK |
| State/compatibility | Protocol immutable history/retry/invalidation | Proposal riêng cho rev/revision, RETRY/caller-halt khi được giao | Không sửa source hoặc chạy fixture từ task IA |
| W4 readiness | W4 plan run42, I05 verified non-target run43 và readiness reconcile blocked run44 | Xem [W4 gap register](w4-readiness-plan.md); đóng gate đúng thứ tự, map I01–I05 và source/state compatibility; runtime chưa đủ điều kiện | G1/G2 incomplete, G3 not run, G4 blocked; profile/cap chưa chọn |
| Runtime / pilot | Design và prerequisite | Chọn consumer LLM thật, profile/target/authority/numeric budget, applicable pair/gates; R4a trước attempt | BLOCKED/NOT_RUN theo dependency; không thay Stage1 parser bằng LLM ngầm |
| Training | Guide/checklist có điều kiện | Chứng minh observed need, rights/ground truth/splits, model eligibility và explicit job scope | NOT_RUN; training không sửa parser/broker hoặc tự tạo quyền |

Nhánh consumer packet là đề xuất offline gần nhất sau logic review. Không lặp lại selected-consumer projection như chưa tồn tại; dùng nguồn đã pin và kiểm lại drift. B4 là một task độc lập, không lồng correction vào thay đổi IA hoặc tự gọi PASS sau sửa một case.

Các câu hỏi cần quyền hoặc dữ kiện mới được giữ trong [open questions](../reference/open-questions.md). Phần độc lập đã được giao có thể tiếp tục khi nhánh khác thiếu prerequisite.
