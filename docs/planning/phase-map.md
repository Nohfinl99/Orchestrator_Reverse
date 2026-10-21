# Bản đồ phase và dependency

Project có **W0–W7** trong bộ Prompt Stack và **R0–R6** trong roadmap cải thiện. Stack 00 là bootstrap, stack 09 là review/handoff. G1–G4 và P1 là gate/acceptance riêng. Các hệ này không tương đương và không được đổi tên qua IA.

## W — Các họ instruction được giữ nguyên

| Phase / stack | Mục tiêu nguyên bản | Protocol | Trạng thái được chứng minh |
|---|---|---|---|
| [00 bootstrap](../../prompt_stacks/00_bootstrap.md) | Intake ý định, phạm vi, DAG và atomic handoff | [Intake](../../prompt_stacks/protocols/intake_protocol.md) | Tài liệu offline |
| [W0 baseline](../../prompt_stacks/01_W0_context_baseline.md) | Baseline, nguồn/revision, scope và phục hồi | [Baseline](../../prompt_stacks/protocols/baseline_protocol.md) | Tài liệu offline; milestone chưa được đóng bởi file này |
| [W1 routing](../../prompt_stacks/02_W1_masters_prompts.md) | Owner, prerequisite, no-match/conflict/stop | [Routing](../../prompt_stacks/protocols/routing_protocol.md) | Tài liệu offline; chưa nối loader |
| [W2 knowledge](../../prompt_stacks/03_W2_knowledge_transfer.md) | Bundle có quyền/nguồn/applicability và consumer ACK | [Knowledge](../../prompt_stacks/protocols/knowledge_protocol.md) | Tài liệu offline; chưa tạo admitted KB/ACK |
| [W3 REA–IDA](../../prompt_stacks/04_W3_REA_IDA.md) | Bảo toàn engine ownership và tám boundary | [Pair](../../prompt_stacks/protocols/pair_protocol.md) | Chưa authentic full-flow target pair |
| [W4 integration](../../prompt_stacks/05_W4_integration.md) | Checkpoint, immutable history, resume/invalidation/retry | [State](../../prompt_stacks/protocols/state_protocol.md) | Runtime NOT_RUN_BLOCKED |
| [W5 evaluation](../../prompt_stacks/06_W5_evaluation.md) | R4a freeze trước attempt, R4b độc lập sau raw | [Evaluation](../../prompt_stacks/protocols/evaluation_protocol.md) | Yêu cầu thiết kế; không có execution mới từ IA |
| [W6 pilot/release](../../prompt_stacks/07_W6_pilot_release.md) | Pilot một role có điều kiện rồi mở rộng/rollback | [Pilot](../../prompt_stacks/protocols/pilot_protocol.md) | Chưa pilot/release từ bộ tài liệu |
| [W7 training](../../prompt_stacks/08_W7_training_conditional.md) | Readiness, rights, split/eval và job authorization | [Training](../../prompt_stacks/protocols/training_protocol.md) | Conditional; NOT_RUN |
| [09 review/handoff](../../prompt_stacks/09_review_gate_handoff.md) | Review đúng digest, gate summary và bàn giao | [Handoff](../../prompt_stacks/protocols/handoff_protocol.md) | Tài liệu offline; không tự sinh acceptance |

Mười file không phải mười lần execution hoặc 57 template đã hoàn thành. Các protocol đang mô tả điều kiện áp dụng; thứ tự đọc file không tự cấp dispatch.

## R — Roadmap cải thiện trong hồ sơ local

Nguồn của bảng này là roadmap revision 3 và các report bổ sung được định danh trong [source map](../reference/source-map.md). Bảng là view điều hướng; không phải bản contract thay thế roadmap.

| Phase | Công việc / đầu ra | Dependency và giới hạn |
|---|---|---|
| R0 baseline/identity | Inventory, source pins, legacy ↔ proposal coverage và gap bốn yêu cầu | Đã có inventory/report offline; không migrate A0–A7 hoặc suy toàn milestone PASS |
| R1 controller/contract | Intake/routing, master/owner/stop/trace và compatibility | Đã có tài liệu và selected-consumer projection; packet admission còn thiếu; B4 riêng trước implementation phụ thuộc |
| R2 knowledge/exemplar | Một bundle có source/rights/applicability, retrieval và ACK | Thiếu rights/admission/ACK thì chỉ catalog metadata; G2 chưa đóng |
| R3 pilot một role | Candidate dự kiến Triage, prompt/KB/caller binding | Chỉ chạy sau R4a đã freeze và prerequisites/model/target/authority/budget phù hợp |
| R4 benchmark/diagnosis | R4a cases/oracles/input/environment/budget trước run; R4b grading sau | R4a trước R3 attempt dù số phase lớn hơn; không sửa oracle sau output |
| R5 checkpoint/backtrack | Prototype theo boundary đã review, immutable attempts và transitive invalidation | Thiết kế sớm ở R1, cases ở R4; cần evidence transitions; restore bytes không thành semantic repair |
| R6 mở rộng/handoff | Áp candidate đã review sang role khác theo dependency | Mỗi role có evidence riêng; pilot PASS không suy toàn hệ PASS |

Không ấn định một “current phase” duy nhất: hồ sơ đang có R0/R1 preparation và các proposal; R2–R6 có prerequisite chưa đủ. Xem [work queue](work-queue.md) để chọn đúng nhánh hiện hành.

## Dependency cần nhớ

- Packet consumer đầy đủ → review/compatibility → xét implementation đúng scope. Proposal hiện chưa dispatch.
- B4 correction mới + review riêng → chỉ mở phần caller boundary phụ thuộc B4.
- Rights/admission + consumer KB ACK → xét knowledge bundle theo G2.
- Authentic applicable REA–IDA pair + G1/G2/G3, profile/quyền/budget + accepted R4a → xét runtime attempt. R4b đến sau raw.
- IA và custody checks không thay bất kỳ dependency nghiệp vụ nào trên đây. [Gate snapshot](../../context/current.md) giữ nguyên.
