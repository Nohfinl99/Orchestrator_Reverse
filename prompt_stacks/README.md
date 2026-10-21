# Prompt Stack index

Các file này là instruction overlay theo trách nhiệm, chưa tự đăng ký agent hoặc kết nối active loader. Protocol chi tiết nằm trong `protocols/`.

| File | Mục đích |
|---|---|
| [00_bootstrap.md](00_bootstrap.md) | Tiếp nhận mục tiêu và lập dependency DAG. |
| [01_W0_context_baseline.md](01_W0_context_baseline.md) | Baseline, scope và revision. |
| [02_W1_masters_prompts.md](02_W1_masters_prompts.md) | Role routing, owner và điều kiện dừng. |
| [03_W2_knowledge_transfer.md](03_W2_knowledge_transfer.md) | Provenance/quyền knowledge và ACK. |
| [04_W3_REA_IDA.md](04_W3_REA_IDA.md) | REA–IDA qua boundaries. |
| [05_W4_integration.md](05_W4_integration.md) | Checkpoint/resume/backtracking. |
| [06_W5_evaluation.md](06_W5_evaluation.md) | R4a/R4b evaluation lifecycle. |
| [07_W6_pilot_release.md](07_W6_pilot_release.md) | Pilot/release prerequisites. |
| [08_W7_training_conditional.md](08_W7_training_conditional.md) | Fine-tuning có điều kiện. |
| [09_review_gate_handoff.md](09_review_gate_handoff.md) | Review/gate/context handoff. |

## Protocol riêng

| Protocol | File |
|---|---|
| Intake | [intake_protocol.md](protocols/intake_protocol.md) |
| Baseline | [baseline_protocol.md](protocols/baseline_protocol.md) |
| Routing | [routing_protocol.md](protocols/routing_protocol.md) |
| Knowledge | [knowledge_protocol.md](protocols/knowledge_protocol.md) |
| REA–IDA pair | [pair_protocol.md](protocols/pair_protocol.md) |
| State/retry | [state_protocol.md](protocols/state_protocol.md) |
| Evaluation | [evaluation_protocol.md](protocols/evaluation_protocol.md) |
| Pilot | [pilot_protocol.md](protocols/pilot_protocol.md) |
| Training | [training_protocol.md](protocols/training_protocol.md) |
| Review/handoff | [handoff_protocol.md](protocols/handoff_protocol.md) |

`DOCUMENT_ONLY` không phải execution receipt. Mỗi task thực tế cần input, owner, authority, predicate và output cụ thể; task target-dependent cần applicable pair và gate.
