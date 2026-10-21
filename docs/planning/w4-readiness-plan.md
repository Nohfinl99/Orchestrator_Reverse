# W4 integration: gap register và thứ tự hoàn tất

**Snapshot:** 21/10/2026. **Trạng thái runtime:** `NOT_RUN_BLOCKED`. **Tác dụng của trang:** lập bản đồ công việc và evidence; không dispatch task, thay contract, đổi runtime hoặc đóng gate.

## Kết luận ngay

W4 đã có `PASS_OFFLINE_PREPARATION_PLAN_ONLY` ở run42; I05 đã có `VERIFIED_NON_TARGET_PREPARATION` ở run43; run44 ghi `RECONCILED_BLOCKED_RUNTIME` sau 83 kiểm tra digest không drift. Đây là chuẩn bị/checkpoint của record có sẵn. Chúng không chứng minh invocation model/REA/IDA, luồng task đầu-cuối, resume/backtracking hoặc acceptance G4 đã chạy.

Gate kế thừa: G1 `INCOMPLETE`, G2 `INCOMPLETE`, G3 `NOT_RUN`, W4 readiness xếp G4 `NOT_RUN_BLOCKED`; bảng tổng hợp `docs/project-status.md` ghi G4 `NOT_RUN`. Đây là phạm vi báo cáo khác nhau, cả hai đều không phải PASS. Provider/model/transport và numeric token/cost cap chưa chọn; v3 `OFF`. Bốn node I01–I04 đều `eligible=false` trong W4 readiness run44. I05 chỉ đủ cho checkpoint của record đã xác minh, không đóng runtime.

## Gaps cần đóng

| ID | Còn thiếu | Evidence cần để đóng | Chủ sở hữu trách nhiệm hiện có |
|---|---|---|---|
| W4-01 / G1 | Versioned alias/identity coverage; role prompt assembly/bindings/manifest; caller/upstream admission và custody; C2/C3–C5, version/broker; walkthrough CTX01–07 từng role. Template I01–I05 còn ghi role A0/A1/A4; mapping đó chưa cấp identity/dispatch mới. | Source-bound candidate; map template về sáu identity hiện hữu bằng source evidence; current upstream integrity/admission/caller records; per-role acceptance và exact-revision independent G1 review. P1J 53/53 chỉ đóng bounded subset. | Prompt-Master điều phối; owner code/contract hiện hữu; reviewer khác producer |
| W4-02 / G2 | WHAT–WHY–HOW modules được review theo source/rights; TRANSFER01–07; ACK hiện hành cho bundle/context/digest của từng consumer | Bundle versioned có quyền/applicability và review; transfer evidence; consumer ACK gắn exact digest. Metadata/custody đơn lẻ không đóng gate. | Curator responsibility hiện hữu và từng consumer; Evidence-Synthesizer review |
| W4-03 / G3 | Target/component/slice và acquisition scope được xác định; authentic producer/session/revision/custody/freshness; REA+IDA cùng target/component/slice/IDA state; PAIR01–12; xác thực và ACK theo consumer | Một vertical slice được cấp quyền và thu thật, pair cùng state, các receipt kiểm fresh/related bởi từng consumer và independent G3 acceptance. Offline fixtures không chứng minh authenticity/live IDB state. | REA/IDA owner theo quyền sẵn có; từng consumer; reviewer G3 |
| W4-04 / Profile | Provider/model/version/transport, host interface, model/pricing evidence, numeric token/cost cap và invocation/response telemetry | Một run profile cụ thể được chọn, pin và giới hạn được phê chuẩn. Chưa có lựa chọn trong hồ sơ; task IA không tự chọn. | Prompt-Master lập profile; user cung cấp quyết định còn thiếu theo quy trình hiện hành |
| W4-05 / State projection | `context_checkpoint_engine.py` được review tĩnh là ghi `rev`, trong khi formatter đọc `revision`; nhãn `Verified` khi load không chứng minh nguồn đã được revalidate. Validator có nhánh `RETRY` cần khớp caller-halt. Immutable attempt, node/dependency/ACK bindings và invalidation runtime chưa được chấp nhận end-to-end. | Một proposal sửa compatibility riêng, source pins mới, migration/backward-compatibility decision của owner contract, rồi negative/positive cases và R4a trước fixture. Sau đó R4b từ raw attempt bởi người khác. Không coi đây là lỗi runtime đã quan sát hoặc tự sửa ở đây. | Owner state/caller hiện hữu; Prompt-Master điều phối; Evidence-Synthesizer/reviewer độc lập |
| W4-06 / G4 | G1+G2+G3 PASS; I01–I04 được chấp nhận; invocation receipts thực; timing/cost/status telemetry; end-to-end state, resume/backtracking evidence | Run được cấp quyền, profile/cap, R4a freeze trước attempt, raw invocation và state transitions, R4b độc lập, rồi G4 acceptance theo đúng scope. | Các owner trên, executor có quyền, evaluator/reviewer khác |

B4 P1K còn `FAIL`. Giữ correction thành revision và review riêng. B4 chặn phần caller-boundary phụ thuộc vào contract này; không tự suy rằng B4 là thay thế hoặc bằng chứng đóng G1/G2/G3.

## Trạng thái năm work item gốc

| Work item | Mục tiêu gốc | Điều kiện vào | Trạng thái hiện có / phần thiếu | Điều kiện acceptance |
|---|---|---|---|---|
| I01 | Thiết kế **một cạnh** của pipeline | G1 + G2 + G3 | Chưa đủ điều kiện; cả ba gate đang mở. Không chọn cạnh/owner theo phỏng đoán. Có thể chỉ chuẩn bị NON_TARGET tài liệu theo task riêng. | Một DAG edge, source/input pins, predicate ID, scope/evidence và một output candidate; independent X01. READY khi gate/dependency hợp lệ. |
| I02 | Thiết kế transport contract cho **một provider** | G1 + provider/model dự án được chọn | Chưa đủ G1, chưa chọn model/provider/host interface. | Một transport candidate có interface/version/source refs/caller boundaries/errors/telemetry; independent X01. Không gọi provider bằng việc lập contract. |
| I03 | Lập budget cho **một run profile** | I02 được nhận; cost limit được giải quyết | Chưa đủ I02, pricing evidence và numeric cap. | Budget record pin model/pricing/version/token/cost cap và stop behavior; independent X01. Không tự điền số. |
| I04 | Thiết kế telemetry schema cho **một event type** | G1 + G3 | Cả G1/G3 chưa đóng; invocation thật và pair chưa có. | Một loại event có provenance, scope, source/run revisions, state/result/error, timing/cost khi có, capture, redaction/rights; independent X01. Chỉ schema design không chứng minh event đã xảy ra. |
| I05 | Lập run manifest từ execution record đã có | Applicable verified records | Run43 có `VERIFIED_NON_TARGET_PREPARATION`; run44 readiness cũng ghi verified prep. Reuse chỉ sau kiểm pin/revalidation cho đúng scope. Không phải runtime PASS hoặc permission cho attempt mới. | Manifest chỉ ghép record bất biến đã tồn tại với exact pins, unknowns và non-target status khi phù hợp; independent check chứng minh không bịa trường/receipt. |

Tên/đầu ra I01–I05 là template gốc trong snapshot, không là task READY. Catalog gốc ghi cả 57 mục là `TEMPLATE_NOT_EXECUTED`. Phân biệt task có thể soạn design offline với node được phép dispatch và execution thật.

## Dependency và thứ tự triển khai

```text
Inventory/revalidate source refs
  ├─ B4 correction + independent design review (riêng; trước phần phụ thuộc B4)
  ├─ G1 source/identity/caller/binding/CTX closure ─┬─ I02 + selected provider/model
  │                                                │    └─ I03 + accepted numeric budget
  │                                                └─ I04 + G3
  ├─ G2 rights/modules/TRANSFER01–07/consumer ACK  ─┐
  └─ G3 authentic authorized REA–IDA pair/PAIR01–12 ┼─ I01 / I04 applicable branch
                                                    └─ I01–I04 + real receipts/telemetry → G4

Existing verified records ───────────────────────────────→ I05 non-target checkpoint
```

Đây là dependency theo readiness run44 và template I01–I05; nhánh thiết kế không target vẫn phải ghi `NON_TARGET_PREPARATION`, `pair=null`, `NOT_RUN`. Không bắt chạy runtime để sắp xếp tài liệu, cũng không dùng thiết kế offline để đánh dấu node runtime READY. Execution task cần input path/digest/revision, output, acceptance, owner/ reviewer, budget, dependencies và stop condition đầy đủ.

## Checkpoint và handoff W4 phải ghi được

Khi đủ điều kiện, mỗi transition cần lưu: `task_id`; owner gửi/nhận và roster tham gia thật; goal/scope và context revision; immutable attempt ID; prompt/role/knowledge/model/tool version và digests; dependency DAG/revisions; G1–G4/predicate refs; authority/scope và applicable REA–IDA pair; từng consumer validation/ACK; invocation và event/exit/timing/cost receipts; trạng thái, finding/unknowns; retry count/cap/progress; transitive nodes/ACK bị invalidated; next owner và điều kiện mở lại. Mỗi lần thử tạo record mới; state đổi thì revalidate dependent receipts. Không ghi chain-of-thought hoặc đặt trạng thái `Verified` chỉ khi load/restore.

Consumer nhận handoff phải kiểm binding, applicability, freshness và output schema theo contract; xác nhận ACK gắn context/bundle/evidence digest, hoặc trả rõ các trường thiếu. ACK của một role không thay ACK role khác. Fail/blocked quay đúng owner được source chỉ ra; thiếu locator giữ root cause `UNRESOLVED`.

## Ranh giới nghiệm thu

- **Design:** file/contract/source mapping được review. Không phải code hoặc run.
- **Implementation:** integration thật ở revision được pin, có compatibility review. Không suy từ prompt/adapter prototype.
- **Execution:** accepted R4a trước attempt; raw command/environment/times/stdout/stderr/child-wrapper-outer exits và run receipts sau attempt.
- **Review:** R4b reviewer khác producer/executor, oracle freeze đúng digest, kết quả từng requirement và gate. Custody hash không thay semantic review.
- **Gate:** G1/G2/G3/G4 đánh giá theo evidence/acceptance gốc và scope. Không cộng số fixture cũ vào readiness chung.

## Next atomic task khả thi ngay

Trang này là **W4 gap/readiness packet** để tiếp nhận một task offline có scope hẹp: nó trỏ run readiness và template đã pin, ghi I01–I05 applicability, gate findings, dependency và tiêu chí; nó không dispatch W4 hoặc đóng B4/G1–G4. Tiếp theo, chọn một task riêng cho B4 amendment, G1/G2 source mapping hoặc state/caller compatibility proposal; implementation/execution của các nhánh phụ thuộc giữ blocked tới khi có prerequisite tương ứng. I05 existing verified preparation có thể được tham chiếu khi pins vẫn khớp.

Để mở branch runtime, cần: (a) G1/G2 evidence; (b) user-selected provider/model/host interface và numeric cap cho I02/I03; (c) scoped target/acquisition authority và fresh G3 pair cho target-dependent I01/I04; (d) acceptance/oracle/executable/input pins cùng budget đóng R4a trước mọi attempt. Thiếu một điều kiện thì branch phụ thuộc `BLOCKED`/`NOT_RUN`, phần tài liệu độc lập vẫn tiếp tục.

## Nguồn đã bind

Năm file đầu dưới `archive/RE-Decom/` đã so với `metadata/migration_manifest.json` của workspace cha và khớp bytes tại thời điểm lập kế hoạch. Report R0 cuối được pin riêng trong `evidence/r0_inventory/20261021_selected_role_01/manifest.json`. Path là workspace-relative từ root `Orchestrator/`; clone public không mang theo các file này.

| Workspace path | SHA-256 | Vai trò |
|---|---|---|
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/01_control_plane/prompt_stacks/handoff_atomic_v1/05_W4_integration.md` | `1e2eef0e0bf02e41f65c68f2af43c6f077ff608d9fd4c5e0b512324fc9e3d562` | Template gốc I01–I05 |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/01_control_plane/prompt_stacks/handoff_atomic_v1/TASK_CATALOG.json` | `3a04a1017b7321711ebf5461190f838533735a6c6c61b818231a096f391acdab` | Template không phải execution |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/04_artifacts/implementation_runs/20261020_gate_closure_meeting_44/W4_gate_readiness.json` | `1d5e1fad56b1990239151e3b15ca773c16a9e15005fab615e097d284cbb7aa3e` | Trạng thái I01–I05/G1–G4 run44 |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/04_artifacts/implementation_runs/20261020_p1k_caller_boundary_design_43/gate_W4_I05.json` | `047eefc91920d8d54ec25562f16471fb16d2e429fe5487d9284b5366db683bab` | I05 `VERIFIED_NON_TARGET_PREPARATION` |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/04_artifacts/implementation_runs/20261020_p1k_caller_boundary_design_43/run_manifest.json` | `3d41886c31aa7568520f1efc280abc387aacfefa6e86f3ebade94e32b1f1f11f` | Record được I05 checkpoint |
| `evidence/r0_inventory/20261021_selected_role_01/report.md` | SHA-256 `a5c0c3d3ea851f62055e7da23ed69961d2bef9e782679484a4c1833dc9c69855` | `rev`/`revision`, Verified/revalidation, RETRY/caller-halt concern; static, không phải runtime finding |

Status/gap derivation được tách khỏi source bytes. Gate cụ thể quyết định qua report/run revision đã bind; plan này tự không chứng nhận tính đầy đủ của inventory hoặc semantic acceptance.
