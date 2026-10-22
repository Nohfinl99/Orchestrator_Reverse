# Biên bản họp tiền triển khai: prompt stack, gate và benchmark

| Trường | Giá trị |
|---|---|
| Meeting ID | `AGENT_OFFICE_PREFLIGHT_REVIEW_20261022_01` |
| Input | `AGENT_OFFICE_PRODUCT_ROADMAP_01` + exact stacks/protocols + W4 readiness |
| Meeting type | `DESIGN_REVIEW / ADVISORY_MULTI_REVIEWER` |
| Dispatch to project six identities | `NO`; project prompt/runtime is not integrated |
| Output | Preflight knowledge and benchmark plan; no execution |

## Agenda

1. Stack routing: what to read for intake, baseline, routing, knowledge, REA–IDA, state, evaluation, pilot and handoff.
2. Gate applicability: which project gates are relevant to offline UI and which are prerequisites for runtime.
3. Review cadence: meeting rounds vs document review rounds vs benchmark attempts/runtime retries.
4. Benchmark design: offline correctness, UI behavior, user value, and future runtime metrics.
5. Next action and stop conditions.

## Debate record

### Position A — Prepare only what the next objective needs

Nạp Stack 00/01/02 để mở AO-1: intake/DAG, exact source revision, owner routing. Dùng Stack 06/09 để đóng benchmark acceptance và review/handoff. Chỉ nạp Stack 03 khi chọn knowledge bundle/consumer; Stack 04 chỉ target-bound REA–IDA; Stack 05 khi state/checkpoint/retry integration; Stack 07 pilot; Stack 08 training. Giữ stacks offline, không coi đây là runtime tool.

### Position B — Không dùng gate project như scorecard cho UI demo

Một offline 3D prototype có thể được kiểm ở level sản phẩm bằng fixture local. Nó không cần giả vờ đã đóng G1–G4. Tuy nhiên, khi liên kết vào caller/runtime/target thật, gate gốc và applicability của W4 trở lại làm blocker. R4a/R4b là quy tắc evaluation cho execution, không phải đồ họa UI.

### Position C — Benchmark phải có đối chứng và oracle

Độ đúng deterministic đo bằng expected transition pinned trước run. UX cần 3D vs 2D cùng scenario và baseline, đo lỗi và tác vụ chứ không hỏi “thích 3D không” đơn thuần. Threshold UX chưa có thì phải để mở, không tự điền số. Chỉ khi read-only/live/control mới đo latency, cost và authority errors.

## Adjudication

- Dùng mapping stack cụ thể trong `preflight-knowledge-and-benchmark.md`; không nạp cả corpus mặc định.
- Tách AO acceptance khỏi G1–G4 và R0–R6/W0–W7. Không nâng gate bằng số lượng card, test, review hoặc fixture.
- Chốt flow đánh giá: intake/source pins → author acceptance/oracles → bounded adversarial review → accepted/frozen R4a → authorized bounded run → independent R4b from raw → human/orchestrator decision.
- Cuộc họp thiết kế khuyến nghị 4 lượt có structured outputs. Tối đa 2 document-review rounds là limit riêng theo stack; runtime retry có cap riêng và không được suy ra từ meeting rounds.
- Bắt đầu bằng AO-1 `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01`. Chưa code/test/benchmark cho tới khi packet được review và có implementation task được người điều phối chấp thuận.

## Decisions / unresolved issues

| Item | Decision/status | Evidence needed to reopen |
|---|---|---|
| Offline 3D/evidence/replay plan | `CONDITIONAL_GO_TO_AO4` | AO-1–AO-4 deliverables/acceptance; R4a/R4b for executions |
| G1/G2/G3/G4, B4, W4 | Preserve current snapshot; no promotion | Exact source-bound new evidence and independent gate review under original contracts |
| Benchmark thresholds | `OPEN` until baseline | AO-1 freeze and AO-4 baseline/user task results |
| Tools/versions | `CANDIDATE_OPTIONS_NOT_SELECTED` | AO-1 contract + authorized spike/owner |
| Live bridge/command control | `BLOCKED_FUTURE` | Producer/caller, authority/scope/budget, security and project prerequisites |
| Knowledge cards runtime admission | `NOT_ADMITTED / NO_ACK` | Rights/applicability/context binding and actual consumer ACK |

G4 status must retain the current snapshot label and readiness report's `NOT_RUN_BLOCKED` scope note; this review does not reconcile the existing status discrepancy. Reviewer recommendations are not project identity ACKs or runtime dispatch receipts.

## Sources read for this review

- `AGENTS.md`, `context/current.md`, `docs/planning/phase-map.md`, `work-queue.md`, `w4-readiness-plan.md`.
- `prompt_stacks/00_bootstrap.md`, `01_W0_context_baseline.md`, `02_W1_masters_prompts.md`, `03_W2_knowledge_transfer.md`, `04_W3_REA_IDA.md`, `05_W4_integration.md`, `06_W5_evaluation.md`, `07_W6_pilot_release.md`, `09_review_gate_handoff.md`.
- `prompt_stacks/protocols/intake_protocol.md`, `baseline_protocol.md`, `routing_protocol.md`, `knowledge_protocol.md`, `pair_protocol.md`, `state_protocol.md`, `evaluation_protocol.md`, `pilot_protocol.md`, `handoff_protocol.md`.
- `docs/reference/validation-status.md`, `docs/knowledge/README.md`, office roadmap/verification plan/profile.

No code, tests, fixture, benchmark, provider, target, training or W4 execution was run.
