# AO-1 test and review matrix — candidate revision 2

| Field | Value |
|---|---|
| Matrix ID | `AGENT_OFFICE_AO1_MATRIX_02` |
| Candidate | `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01:2-candidate` |
| Status | `DESIGN_MATRIX / NOT_FROZEN / NOT_RUN` |
| Authority | Advisory candidate; no acceptance, dispatch, or project gate effect |

## Use and limits

This matrix maps requirements to proposed offline cases and observable oracles. It is a planning artifact, not a test result. All verdicts are `OPEN`; all execution is `NOT_RUN`. Do not run or validate the synthetic fixture until a separate applicable R4a record is reviewed, accepted, and frozen with exact candidate/schema/input/oracle/environment/budget/authority. After an authorized bounded attempt, an independent R4b reviewer must assess preserved raw evidence. A matrix row does not itself authorize an attempt.

The three intended fixture cases are: **C01** parallel work plus bounded dissent; **C02** cancellation before synthesis; **C03** a separate synthetic budget-limit stop. Proposed event names and transitions are used below; exact event locators must be added from the final frozen fixture. Never infer a missing event or state.

## Requirements-to-case matrix

| ID | Requirement / stimulus | Case and event path | Expected oracle / observable result | Hard failure | Design review | Future execution |
|---|---|---|---|---|---|---|
| `M-01` | Exactly the six current identities; no new identity, alias, or seventh Orchestrator avatar | C01/C02/C03 seed | Six unique canonical names only; Orchestrator remains a function | Extra, duplicate, or unknown identity; Orchestrator displayed as an agent | `OPEN` | `NOT_RUN` |
| `M-02` | Parallel tasks with independent work state | C01 task assignment then status change for Triage-Sentinel and Product-Evolution-Architect | Both task IDs remain independently `working`; assignment and working are distinguishable | Assignment alone shown as working; one task overwritten or lost | `OPEN` | `NOT_RUN` |
| `M-03` | Invite to busy agent; defer without preemption | C01 Product-Evolution-Architect existing task → invite → defer | Invite precedes defer; task stays assigned/working at desk; participant is not in room | Missing invite; task cleared/preempted; deferred shown as joined | `OPEN` | `NOT_RUN` |
| `M-04` | Invite/accept/join are distinct and visible | C01 Prompt-Master and Evidence-Synthesizer participation chains | Only identities with join events are attendees; each contribution has joined author | Invite or accept treated as join; contribution from non-joined author | `OPEN` | `NOT_RUN` |
| `M-05` | Contribution with claim and missing evidence | C01 Prompt-Master structured contribution, `CLM-01` | Claim author and meeting link retained; empty refs shown as `NO_EVIDENCE_REF` | Missing provenance styled as sourced/verified | `OPEN` | `NOT_RUN` |
| `M-06` | Objection references a specific claim | C01 Evidence-Synthesizer objection `OBJ-01` → `CLM-01` | Click-through preserves objection, claim, author, and evidence refs | Objection detached, hidden, or attributed to wrong identity | `OPEN` | `NOT_RUN` |
| `M-07` | Synthesis retains dissent and open question | C01 synthesis after contributions | Agreements remain empty; dissent, unsupported claim, and question remain visible; candidate is not approval | Majority/consensus inferred; dissent erased; DAG/gate changes | `OPEN` | `NOT_RUN` |
| `M-08` | Exact duplicate event is idempotent | C01 repeat byte-identical event ID | One state transition/action; duplicate diagnostic is visible | Duplicate action/count/motion, or duplicate records differ | `OPEN` | `NOT_RUN` |
| `M-09` | Same ID with conflicting content | C01 conflict policy case if included in frozen input | Conflicting record is quarantined and diagnosed, with no state mutation | Silent overwrite/merge or treated as harmless exact duplicate | `OPEN` | `NOT_RUN` |
| `M-10` | Out-of-order sequence and late event | C01 sequence inversion with a late event filling one provisional gap | Arrival order is retained; filled gap closes with diagnostic; reducer never rolls back newer state | Silent sorting, rollback, or stale result overwrites newer state | `OPEN` | `NOT_RUN` |
| `M-11` | Unresolved sequence gap at end of replay | C01 one absent sequence before close | Final gap remains visibly open; last known state is marked with uncertainty as designed | Gap hidden or falsely resolved | `OPEN` | `NOT_RUN` |
| `M-12` | Stale heartbeat/presence | C01 stale event after participation; any late heartbeat is sequence-aware | Presence changes independently; work/meeting/location facts do not change; stale remains correct at highest sequence | Stale becomes failed/completed or old heartbeat restores live state | `OPEN` | `NOT_RUN` |
| `M-13` | Turn-limit stop | C01 close at configured turn cap | Explicit `turn_limit` reason, final turn, and sub-cap synthetic usage; no approval/completion | Stop treated as consensus, approval, or task completion | `OPEN` | `NOT_RUN` |
| `M-14` | Meeting cancellation | C02 proposed → invited → accepted → joined → cancelled before synthesis | Cancellation reason/last turn retained; no synthesis/completion; location does not change without explicit return event | Cancel treated as completion or unlogged movement | `OPEN` | `NOT_RUN` |
| `M-15` | Budget-limit stop distinct from turn limit | C03 separate meeting closed at synthetic cap | Explicit `budget_limit`, synthetic used equals synthetic limit; no approval/completion | Confused with turn stop or actual cost | `OPEN` | `NOT_RUN` |
| `M-16` | Event provenance and simulation marker | Every event in C01–C03 | `SIMULATED`, candidate revision, case ID, event ID, sequence, timestamp and synthetic locator present | Missing simulation/provenance or live implication | `OPEN` | `NOT_RUN` |
| `M-17` | Schema constrains roster and agent references | All cases | Roster contains each canonical identity once; every agent ref belongs to the six-name set | Duplicate roster item, alias, or arbitrary identity accepted | `OPEN` | `NOT_RUN` |
| `M-18` | Unknown event/schema handling | Negative case to be added only if frozen in R4a | Unsupported state is explicit and cannot become success | Unknown event silently treated as successful transition | `OPEN` | `NOT_RUN` |

## Visual, privacy, and accessibility matrix

| ID | Observable check | Future evidence | Hard failure | Verdict |
|---|---|---|---|---|
| `UX-01` | Persistent `SIMULATED · OFFLINE` in header and detail surfaces | Screenshot/video plus DOM/accessibility tree | Label absent, hidden on a view, or implies live agent | `OPEN / NOT_RUN` |
| `UX-02` | Timeline is authoritative and shows arrival index, producer sequence, event ID, actor, task/meeting and anomaly labels | Capture at each relevant event step | Timeline and scene disagree without surfaced conflict | `OPEN / NOT_RUN` |
| `UX-03` | Only event-backed movement; deferred agent remains at desk | C01 scene capture at invite/defer/join checkpoints | Motion implies invite acceptance, work, or completion without event | `OPEN / NOT_RUN` |
| `A11Y-01` | Keyboard-only reachability for replay controls, roster, timeline, details | Recorded keyboard walkthrough and focus order | Required information/action inaccessible without pointer | `OPEN / NOT_RUN` |
| `A11Y-02` | Visible focus and announced selected identity/event/current row | Accessibility tree or screen-reader review notes | Selection/current state cannot be determined non-visually | `OPEN / NOT_RUN` |
| `A11Y-03` | Zoom/pan has reset and keyboard alternatives | Interaction capture | Spatial view becomes trapped or cannot be reset without pointer | `OPEN / NOT_RUN` |
| `A11Y-04` | Reduced motion removes travel while retaining state/event cues | Paired reduced-motion and default captures | Motion required to understand state, or reduced mode hides information | `OPEN / NOT_RUN` |
| `A11Y-05` | 2D roster/table and timeline expose equivalent task, meeting, evidence, dissent, and stop data | Side-by-side field crosswalk and interaction review | Any key field/action exists only in 3D view | `OPEN / NOT_RUN` |
| `A11Y-06` | Status color is paired with text and icon/shape | Visual inspection under color variation | Color is sole status cue | `OPEN / NOT_RUN` |
| `PRIV-01` | No personal data, credentials, hidden prompts, source contents, real transcript, or private chain-of-thought | Fixture/source review | Sensitive or private reasoning included | `OPEN / NOT_RUN` |
| `PRIV-02` | Missing evidence stays missing; local evidence refs are inert | Data/interaction review | UI fabricates evidence or navigates externally in offline mode | `OPEN / NOT_RUN` |

## Evaluation sequence and evidence contract

1. **Before execution (R4a):** freeze candidate and schema revision/digests; exact fixture digest and arrival order; case IDs; expected states and hard failures; environment/tool versions; capture plan; numeric attempt/time/resource cap; authorized scope; executor and independent R4b reviewer. Missing any required field means `BLOCKED / NOT_RUN`.
2. **Bounded attempt:** only after R4a is accepted/frozen and execution is explicitly authorized. Preserve raw input, command/argv, environment, timestamps, output, exit statuses at each wrapper layer, candidate/oracle/input digests, and attempt history. No hidden retries or mutated oracle.
3. **After raw (R4b):** a reviewer independent from author/executor inspects raw evidence and records each matrix row `PASS/FAIL/OPEN` with locator. Any post-freeze change requires a new candidate revision and R4a freeze before another attempt.
4. Separate schema/reducer correctness, visual judgment, accessibility, and later AO-4 usability outcomes. No average score can cancel a hard failure. Screenshot or consensus alone does not establish correctness.

## Project boundary

This matrix does not establish R0–R6 or W0–W7 completion; does not affect P1K B4 `FAIL`, G1/G2 `INCOMPLETE`, G3/G4 `NOT_RUN`, W4 runtime `NOT_RUN_BLOCKED`, or v3 `OFF`; and creates no ACK, receipt, permission, target pair, identity, runtime capability, or gate evidence. Six identities and REA–IDA boundaries remain unchanged.
