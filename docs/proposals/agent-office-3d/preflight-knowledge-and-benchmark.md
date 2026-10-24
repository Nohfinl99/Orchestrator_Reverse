# Gói chuẩn bị trước triển khai: prompt stack, gate và benchmark

| Trường | Giá trị |
|---|---|
| Package ID | `AGENT_OFFICE_PREFLIGHT_01` |
| Roadmap | `AGENT_OFFICE_PRODUCT_ROADMAP_01` |
| Trạng thái | `KNOWLEDGE_PREPARED / BENCHMARK_NOT_RUN / RUNTIME_NOT_READY` |
| Loại | Hướng dẫn điều hướng kiến thức + kế hoạch evaluation; không phải implementation/gate receipt |

## Kết luận review

Có thể chuẩn bị và sau đó làm một prototype offline theo AO-1…AO-4. Nhưng project chưa ở trạng thái cho phép suy ra điều phối agent thật: prompt stack/protocol là instruction offline chưa nối runtime; W4 `NOT_RUN_BLOCKED`; I01–I04 trong readiness run44 không eligible; P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 chưa PASS; v3 `OFF`.

Văn phòng offline không cần đạt G1–G4 chỉ để dựng UI giả lập. Nếu dự án muốn dùng office để quan sát/điều khiển Orchestrator runtime, phải đi qua gate gốc theo đúng applicability và evidence. AO phase không tương đương R0–R6, W0–W7, G1–G4, P1 predicates hoặc W4 items.

## Prompt stack cần nạp theo objective

Không nạp cả bộ mỗi lần. Đọc `AGENTS.md`, current/work queue, rồi chọn đúng stack/protocol. Các stack là overlay tài liệu, chưa phải executable prompt package/runtime.

| Mục tiêu | Stack/protocol | Điều nó kiểm soát | Dùng với văn phòng 3D |
|---|---|---|---|
| Intake, scope, goal, DAG, output/acceptance | `00_bootstrap` + `intake_protocol` | Task phải có objective, owner hiện hữu, input path+digest+revision, output, acceptance predicate, dependency, budget. Thiếu thông tin trọng yếu → `WAIT_INPUT`/`BLOCKED`, không `READY`. | Luôn dùng để lập AO-1 packet và mỗi task |
| Baseline, source/revision, provenance | `01_W0_context_baseline` + `baseline_protocol` | Pin đúng version; mismatch giữ expected/actual và dừng nhánh phụ thuộc; tách baseline, active state, candidate | Luôn dùng khi đọc repo/contract/test candidate |
| Route owner/no-match/stop | `02_W1_masters_prompts` + `routing_protocol` | Chọn trong sáu identity đúng capability; ambiguity/gate thiếu → resolve/blocked; 0 owner chỉ là `NO_MATCH` khi đã kiểm eligibility | Prompt-Master điều phối; Product-Evolution-Architect cho product; Evidence-Synthesizer review; role kỹ thuật khác chỉ khi task phù hợp |
| Knowledge bundle/consumer ACK | `03_W2_knowledge_transfer` + `knowledge_protocol` | Source/rights/applicability, WHAT/WHY/HOW, selected/rejected retrieval, exact bundle/context binding và consumer ACK | Dùng nếu prototype/runtime dùng knowledge module. Candidate cards hiện chưa admitted/ACK; catalog không đóng G2 |
| Target-bound REA–IDA evidence | `04_W3_REA_IDA` + `pair_protocol` | Bảo toàn engine ownership, authentic same target/component/slice/IDA state, custody/freshness/consumer validation | Không áp target pair cho synthetic UI fixture. AO-1/AO-3 ghi `NON_TARGET_PREPARATION`, pair=null, `NOT_RUN`; G3 chỉ khi có target-bound work thực sự |
| Checkpoint/state/retry/resume | `05_W4_integration` + `state_protocol` | Handoff/checkpoint, immutable attempts, invalidation, retry cap/progress/stop | Áp khi tích hợp state/bridge hoặc triển khai resume. W4 runtime hiện blocked; tài liệu này không mở W4 |
| Evaluation và benchmark | `06_W5_evaluation` + `evaluation_protocol` | R4a freeze trước execution; R4b độc lập sau raw evidence; tách design/code/executed/reviewed | Bắt buộc trước mọi benchmark execution, kể cả fixture/mechanical run theo project protocol |
| Pilot/release | `07_W6_pilot_release` + `pilot_protocol` | Scoped role pilot, prerequisites, rollback, rollout | Không dùng cho AO-1/AO-4 UX test; runtime pilot về sau mới cần |
| Training | `08_W7_training_conditional` + `training_protocol` | Rights, ground truth, splits/evaluation, eligibility, explicit job authorization | Không cần để xây offline board; không khởi động training |
| Candidate review/handoff | `09_review_gate_handoff` + `handoff_protocol` | Candidate digest, independent findings, gate summary từ receipts, gaps/next task/reopen conditions | Dùng sau mỗi packet/revision và phase decision |

### Kiến thức tham khảo chọn lọc

Tham chiếu index [Knowledge](../../knowledge/README.md) và [retrieval guide](../../knowledge/prompt-orchestration/retrieval-guide.md). Gợi ý theo task: K01 objective/acceptance; K02 context/source locator; K03 dependency/owner; K04 artifact validation; K06 checkpoint/handoff; K07 evidence/reviewer; K08 prompt/module versioning; K10 edge cases; K11 prompt-vs-tool/authority; K12 scoped retrieval. Đây là `CANDIDATE_REFERENCE_NOT_ADMITTED`; chưa là KB runtime, source rights/consumer ACK còn phải xác thực theo G2 nếu có consumer.

Không ingest toàn corpus; log selected/rejected, reason, exact bundle revision/digest, rights/applicability, locator, missing ACK. Benchmark gold/held-out answers không được đưa vào active knowledge bundle.

## Gate/evaluation map: điều gì làm “đạt”

### Gate của project gốc

- **P1K B4 `FAIL`:** giữ FAIL; correction cần revision riêng, exact digest và review riêng. Không dùng prototype office để chữa hoặc che B4.
- **G1 `INCOMPLETE`:** cần source-bound identity/role/caller/admission/binding và các coverage đúng contract; stack file hoàn chỉnh không đồng nghĩa G1 PASS.
- **G2 `INCOMPLETE`:** cần rights/applicability/review, bundle/context binding, transfer và ACK thật của từng consumer. Knowledge index/card không tự đóng G2.
- **G3 `NOT_RUN`:** chỉ applicable với target-bound authorized REA–IDA work và authentic matching target/component/slice/IDA-state evidence. Simulation/UI không tạo pair hoặc G3.
- **G4 `NOT_RUN` theo current snapshot:** readiness report phân loại G4 `NOT_RUN_BLOCKED`; giữ cả hai locators/scope cho tới khi có nguồn mới giải quyết. Cần G1+G2+G3 applicable PASS, I01–I04/receipts/telemetry và evaluation acceptance đúng contract. Không chuẩn hóa xung đột status bằng suy luận.
- **W4 `NOT_RUN_BLOCKED`; v3 `OFF`:** không gọi runtime hoặc bật v3 từ roadmap sản phẩm.

Readiness run44 ghi I01–I04 `eligible=false`, I05 chỉ verified non-target preparation; đây không phải permission/runtime pass. 26 named CTX/TRANSFER/PAIR criteria và 33 future cases giữ nguyên denominator/status; bổ sung case cho office benchmark không được cộng để tuyên bố gate coverage.

### Khi nào acceptance một phase office là đạt

Ghi từng predicate `PASS`, `FAIL`, `OPEN` hoặc `N/A` có lý do. Acceptance office offline có thể xác nhận schema/reducer/UI của đúng candidate và fixture đã pin; không nâng project gate. Các invariant phần mềm phải đạt trên mọi fixture liên quan, không lấy tỷ lệ trung bình để bỏ qua hard fail:

1. Avatar/state luôn khớp event; không có invite/join/complete khi thiếu event tương ứng.
2. Lệnh pending tách khỏi receipt; agent bận/defer giữ task hiện tại.
3. Mỗi claim/objection mở được participant/event/evidence locator hoặc báo `NO_EVIDENCE_REF/UNSUPPORTED`.
4. Mâu thuẫn vẫn hiện dissent/open question; thiếu participant không bị bịa contribution; không suy consensus từ đa số.
5. Cùng pinned fixture/candidate tạo cùng reducer output; duplicate idempotent; gap/out-of-order/stale không âm thầm lùi trạng thái.
6. `SIMULATED` luôn hiển thị; live/sim không được trộn; transcript chỉ chứa output được phép, không private chain-of-thought.
7. Handoff/decision chỉ tạo action/DAG transition khi có authority/receipt phù hợp.

## Cách benchmark theo lớp

### Benchmark 0 — Freeze trước khi chạy (R4a)

Trước mọi fixture/test execution: freeze candidate/code digest; case IDs; exact JSONL input digest; expected state/view/oracle; positive, negative, blocked hoặc justified N/A; hard fail; environment/tool versions; capture plan; numeric budget/stop cap; reviewer; authority/scope. Nếu R4a chưa accepted thì trạng thái `NOT_RUN`, dù có thể chạy lệnh kỹ thuật. Thảo luận họp không thay R4a.

### Benchmark 1 — Offline state/event correctness

Sau khi có implementation task được chấp nhận: chạy các nhóm fixture đã khóa trong [verification plan](verification-plan.md): command vs receipt; parallel task; busy/defer; accept/join; contribution/objection locator; contradictory claims; missing participant; refusal/failure/cancel; duplicate/out-of-order/gap/reconnect; stale; budget/turn-stop; `SIMULATED` badge.

**Oracle:** bảng expected transition và expected UI state đóng trước run. Ghi event ID/seq/agent/task/meeting, reducer output, raw capture và mọi mismatch. Các invariant 1–7 là hard failures, không bù trừ bằng case khác. Các acceptance source locator hiện vẫn proposed, không phải runtime gate.

### Benchmark 2 — UI behavior/observability

Khi UI đã tồn tại và test task được giao: verify click avatar→detail; event timeline↔scene consistency; meeting panel; pause/step/replay; evidence links; filter/error/empty/stale cases; keyboard/accessible fallback. Kiểm tự động deterministic và visual judgement là hai báo cáo riêng. Không tuyên bố usability từ screenshot/install smoke.

### Benchmark 3 — UX value AO-4

So sánh 3D và bảng/timeline 2D bằng cùng scenario/task list/oracle; đổi thứ tự UI giữa các người thử để hạn chế learning effect. Ghi baseline trước khi chọn threshold. Đo: nhận diện đúng task/agent bị block; phân biệt requested/dispatched/joined; tìm evidence/decision/dissent; thời gian; sai phân loại; task bỏ sót; calibration/tự tin so với đáp án. Chốt ngưỡng sau baseline và người điều phối duyệt; không lấy vote Reddit làm kết quả.

### Benchmark runtime — một nhánh khác

Chỉ sau AO-4 và các quyền/producer/binding/budget/gate prerequisites: invocation receipt, refusal/cancel, event loss/reorder/recovery, event-to-render latency, stale detection, actual token/cost, unauthorized action. Kết quả offline không thể thay hoặc promote G1–G4; cần R4a trước run và R4b độc lập sau.

### R4b review sau run

Reviewer khác producer/executor đọc raw `argv`, environment, timestamps, stdout/stderr, child-wrapper-outer exit, candidate/oracle/input digests và attempt history; đánh giá từng acceptance, ghi `PASS/FAIL/OPEN` và finding/locator. Không suy output thiếu từ exit code con; không dùng hash custody, review consensus, install smoke hoặc historical 53/53 làm project PASS.

## Số vòng họp và số vòng review

Đây là các vòng khác nhau:

- **Cuộc họp thiết kế 4 lượt:** (1) Prompt-Master chốt câu hỏi/scope; (2) Product-Evolution-Architect và người phân tích ghi position riêng; (3) reviewer chất vấn claim/acceptance, nêu phản chứng; (4) Evidence-Synthesizer tách consensus/dissent/unknown và lập options. Người điều phối quyết định. Thảo luận có thể dừng sớm nếu không còn question material, nhưng không bỏ role review bắt buộc.
- **Document review tối đa 2 vòng** theo stack/protocol hiện hành. Sau hai vòng mà còn finding thì `REVISE_NOT_ACCEPTED`/`BLOCKED`; sửa sau review phải tạo candidate digest mới và review lại. Đây không phải runtime retry count.
- **Benchmark:** một R4a freeze trước lần attempt; chạy bounded attempts theo cap đã duyệt; một R4b độc lập sau raw. Nếu cần thay candidate/oracle/input sau freeze, tạo revision mới và freeze lại trước attempt tiếp theo.
- **Runtime retry:** chỉ khi contract cho phép, numeric retry cap được phê duyệt và mỗi attempt tạo record mới/progress evidence; thiếu cap thì `BLOCKED`. Không suy retry cap từ số vòng meeting/review.

## Bộ công cụ chuẩn bị

Chưa cài hoặc chọn phiên bản. Candidate options cho AO-1/AO-3: JSON Schema + validator (ví dụ Ajv) để kiểm event envelope; JSONL synthetic fixtures; pure reducer/deterministic replay; Vitest cho state transition; Playwright cho thao tác browser; Three.js hoặc React Three Fiber cho scene sau spike. Event source contract/toolchain cần được chọn và pin trong AO-1 packet; không có tool nào tự cấp quyền dispatch. AO-4 dùng task sheet và oracle pin; user sessions chỉ sau scope/consent phù hợp. SSE/WebSocket chỉ xét cho AO-5 theo producer/transport contract.

## Những gì chưa làm

- Chưa chạy benchmark, fixture, test, prototype, provider, target, REA/IDA hoặc W4.
- Chưa cài toolchain, chọn model/provider/budget, mở runtime bridge hoặc bật v3.
- Chưa admitted knowledge cards thành KB; chưa ACK consumer.
- Tất cả thẻ/acceptance/benchmark của văn phòng còn proposal cho tới khi task implementation và R4a/R4b đúng quy trình.
