# AO-1 test and review matrix — candidate revision 5

| Field | Value |
|---|---|
| Matrix ID | `AGENT_OFFICE_AO1_MATRIX_05` |
| Candidate | `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01:5-candidate` |
| Input files | `ao-1-fixture-v5.jsonl` and `ao-1-event-v5.schema.json` |
| Status | `DESIGN_MATRIX / NOT_FROZEN / NOT_RUN` |
| Authority | Advisory only; no acceptance, dispatch, or project-gate effect |

## Scope and test boundary

This matrix is a design-to-case crosswalk, not an execution result. Every verdict is `OPEN`; every executable check is `NOT_RUN`. Do not validate or replay the fixture until an applicable R4a is accepted and frozen against exact candidate/schema/input/oracle/environment/budget/authority. After any authorized bounded run, a separate R4b reviewer must assess preserved raw evidence. This artifact does not itself approve a run.

The three cases are C01 parallel work with bounded dissent; C02 cancellation before synthesis; and C03 a separate synthetic budget-limit stop. All rows use local `SIMULATED` data only. Event references below are exact IDs in candidate 5. C01 intentionally repeats `evt-014` twice with identical event content, followed by a third `evt-014` record whose payload differs (`status=joined-conflict`) to exercise a same-ID/content collision. The collision must be quarantined and must not mutate state.

Unknown event types and unsupported schema versions are **deferred to AO-3**. They are not AO-1 acceptance criteria or fixture stimuli.

## Functional requirements crosswalk

| ID | Requirement | Case / exact event locator | Expected oracle | Hard failure | Design | Run |
|---|---|---|---|---|---|---|
| `M-01` | Exactly six existing identities, each unique; no alias or seventh identity | C01 `evt-001`; C02 `evt-101`; C03 `evt-201` | Roster contains Prompt-Master, Triage-Sentinel, Decomp-Analyst, Crypto-Logic-Specialist, Evidence-Synthesizer, Product-Evolution-Architect exactly once | Missing, extra, repeated, aliased identity; Orchestrator shown as agent | `OPEN` | `NOT_RUN` |
| `M-02` | Two independent tasks run in parallel; assignment differs from working | C01 `evt-002`→`evt-003` (`TASK-TRIAGE-17`); `evt-004`→`evt-005` (`TASK-PRODUCT-08`) | Both tasks remain working at desk concurrently; `assigned` alone is not `working` | Work state inferred without event or one task overwrites the other | `OPEN` | `NOT_RUN` |
| `M-03` | Invite busy participant; defer without preemption | C01 `evt-011`→`evt-012` | Product-Evolution-Architect invite precedes defer; existing `TASK-PRODUCT-08` remains working at desk, participant is not attending | Missing invite; task cleared; defer displayed as join | `OPEN` | `NOT_RUN` |
| `M-04` | Invite, accept, join remain separate | C01 Prompt-Master `evt-007`→`evt-008`→`evt-009`; Evidence-Synthesizer `evt-010`→`evt-013`→`evt-014` | Only joined identities appear as attendees | Invite/accept treated as join or unjoined author contributes | `OPEN` | `NOT_RUN` |
| `M-05` | Claim and contribution retain author and missing evidence | C01 `evt-015` (`CLM-01`) | Prompt-Master is joined; claim is linked to meeting and rendered `NO_EVIDENCE_REF` | Unsupported claim styled as verified or sourced | `OPEN` | `NOT_RUN` |
| `M-06` | Objection links to its claim | C01 `evt-016` (`OBJ-01`→`CLM-01`) | Evidence-Synthesizer, claim, objection and empty evidence refs remain linked | Objection detached, hidden, or misattributed | `OPEN` | `NOT_RUN` |
| `M-07` | Structured synthesis retains unresolved dissent | C01 `evt-017` contribution; `evt-018` synthesis | Agreements empty; dissent, unsupported `CLM-01`, open question, `HOLD_FOR_EVIDENCE`, approval false | Consensus/approval inferred; dissent omitted; gate/DAG mutation | `OPEN` | `NOT_RUN` |
| `M-08` | Exact duplicate is idempotent | C01 two byte/content-identical `evt-014` join records (second occurrence) | One join transition/count/motion; duplicate diagnostic shown | Repeat side effect or records differ | `OPEN` | `NOT_RUN` |
| `M-09` | Same-ID, different-content conflict is quarantined | C01 third `evt-014` record (`status=joined-conflict`), immediately after exact duplicate | Conflict diagnostic; conflicting record has no state effect; previously accepted join state remains | Merge/overwrite, extra join/motion, or treated as an exact duplicate | `OPEN` | `NOT_RUN` |
| `M-10` | Out-of-order event and provisional gap | C01 `evt-018` producer `seq=19`, `evt-019` `seq=20`, then late `evt-020` `seq=18` | Preserve arrival order; show inversion; close provisional gap at 18; do not roll back newer state | Silent sort/rollback or late heartbeat makes final state live after later stale event | `OPEN` | `NOT_RUN` |
| `M-11` | Final unresolved sequence gap | C01 close `evt-021`, producer `seq=22` after seq 20/late 18 | Sequence 21 remains visibly missing at end of replay | Gap hidden or falsely resolved | `OPEN` | `NOT_RUN` |
| `M-12` | Presence stale is separate from work/meeting/location | C01 `evt-019` stale (`seq=20`); late `evt-020` heartbeat (`seq=18`) | Highest producer sequence keeps presence stale; work and participation facts stay intact | Old heartbeat restores live state or changes work/meeting state | `OPEN` | `NOT_RUN` |
| `M-13` | Turn-limit stop distinct from budget stop | C01 close `evt-021` | `turn_limit`, turn 2, synthetic usage below cap; no approval/completion | Turn stop implies consensus, approval, or task completion | `OPEN` | `NOT_RUN` |
| `M-14` | Cancellation before synthesis is distinct from completion | C02 `evt-102`→`evt-103`→`evt-104`→`evt-105`→`evt-106` | Cancel reason and last turn retained; no synthesis/completion; no unlogged return movement | Cancellation rendered complete or avatar moves without return event | `OPEN` | `NOT_RUN` |
| `M-15` | Pre-invocation budget stop has an explicit cause and is separate from turn limit | C03 `evt-202` proposal→`evt-203` `meeting.budget_preflight_blocked` (`execution_started=false`, estimate=cap=25/25)→`evt-204` close at turn 0 | Synthetic estimate reaches cap before invocation; close uses `budget_limit`, turn=0, no approval/completion | Close lacks cause; event implies agent ran or turn began; turn/budget conflated; values imply real cost | `OPEN` | `NOT_RUN` |
| `M-16` | Event provenance and simulation label | All events in C01–C03 | Each logical event has an ID; repeated records are explicit duplicate/conflict stimuli. Every record carries case/schema version, ID, seq/time, `SIMULATED`, candidate source revision and synthetic locator | Missing provenance/label or implication of live execution | `OPEN` | `NOT_RUN` |
| `M-17` | Canonical identities constrained by schema | All seed roster and `agent_id` fields | Exactly six unique roster entries; every identity reference is in the canonical six-name enum | Alias, duplicate roster entry, or arbitrary agent ID accepted | `OPEN` | `NOT_RUN` |
| `M-18` | Unknown event/schema stimulus | Deferred to AO-3 | Excluded from AO-1 matrix and acceptance; separate AO-3 case/oracle required | AO-1 acceptance claims unknown-event resilience without a frozen case | `OPEN / DEFERRED` | `NOT_RUN` |

## Visual, accessibility, and privacy matrix

| ID | Observable check | Future evidence | Hard failure | Verdict |
|---|---|---|---|---|
| `UX-01` | Persistent `SIMULATED · OFFLINE` badge in header/detail views | UI capture and accessibility tree | Label absent or implies live session | `OPEN / NOT_RUN` |
| `UX-02` | Timeline reports arrival order, seq, event ID, actor, task/meeting, duplicate/conflict/order/gap/stale/cancel warnings | Captures at C01/C02/C03 checkpoints | Scene and timeline disagree without warning | `OPEN / NOT_RUN` |
| `UX-03` | Avatar motion follows event only; deferred Product-Evolution-Architect stays at desk | C01 captures at `evt-011`/`evt-012`/`evt-014` | Motion implies acceptance, join, work or completion without event | `OPEN / NOT_RUN` |
| `A11Y-01` | Keyboard-only control of replay, roster, timeline and details | Recorded walkthrough and focus sequence | Core state/action inaccessible without pointer | `OPEN / NOT_RUN` |
| `A11Y-02` | Visible focus and announced selected identity/event/current row | Screen reader/accessibility-tree review | Selection/current position cannot be determined non-visually | `OPEN / NOT_RUN` |
| `A11Y-03` | Zoom/pan has reset and keyboard alternatives | Interaction capture | Spatial navigation is trapped or requires pointer to reset | `OPEN / NOT_RUN` |
| `A11Y-04` | Reduced motion removes travel but preserves state/event cues | Paired default/reduced-motion captures | Motion is required to understand state or reduced mode hides data | `OPEN / NOT_RUN` |
| `A11Y-05` | 2D roster/table and timeline expose equivalent task, meeting, claim, evidence, dissent and stop information | Field crosswalk and interaction review | Key information/action exists only in 3D | `OPEN / NOT_RUN` |
| `A11Y-06` | Color is paired with text and icon/shape | Visual review | Color is the only status signal | `OPEN / NOT_RUN` |
| `PRIV-01` | No personal data, credentials, hidden prompts, real transcript, source contents or private chain-of-thought | Fixture/data review | Sensitive information present | `OPEN / NOT_RUN` |
| `PRIV-02` | Evidence links remain local/inert; missing evidence remains missing | Data and interaction inspection | UI fabricates evidence or navigates externally in offline mode | `OPEN / NOT_RUN` |

## Evaluation order

1. **R4a before any execution:** freeze candidate/schema/fixture/oracle digests, exact arrival order, case IDs, hard failures, environment/tool versions, capture plan, numeric attempt/resource cap, authority/scope, executor, and independent R4b reviewer. Missing a required field means `BLOCKED / NOT_RUN`.
2. **Bounded run only after R4a acceptance/freeze and explicit authorization:** preserve raw input, argv/command, environment, timestamps, stdout/stderr, wrapper and child exit statuses, candidate/oracle/input digests, and attempt history. No hidden retry or post-output oracle change.
3. **R4b after raw evidence:** independent reviewer records each row `PASS/FAIL/OPEN` with evidence locator. Any candidate/input/oracle change requires a new revision and new R4a before another attempt.
4. Keep reducer correctness, visual review, accessibility, and future AO-4 usability study as separate results. Hard failures cannot be averaged away.

## Gate and scope boundary

All matrix verdicts are `OPEN`; all execution is `NOT_RUN`. This matrix does not establish R0–R6, W0–W7, P1 predicates, or G1–G4; it does not change P1K B4 `FAIL`, G1/G2 `INCOMPLETE`, G3/G4 `NOT_RUN`, W4 runtime `NOT_RUN_BLOCKED`, or v3 `OFF`. It creates no identity, ACK, receipt, permission, target pair, runtime capability, or project-gate evidence. Six identities and REA–IDA boundaries remain unchanged.
