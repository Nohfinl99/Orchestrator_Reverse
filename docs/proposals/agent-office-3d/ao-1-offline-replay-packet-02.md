# AO-1 offline replay packet — candidate revision 2

| Field | Value |
|---|---|
| Packet ID | `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01` |
| Revision | `2-candidate` |
| Status | `REVIEWED_ADVISORY / REVISE / NOT_ACCEPTED / NOT_RUN` |
| Schema and input | [v2 event schema](ao-1-event-v2.schema.json), [v2 synthetic fixture](ao-1-fixture-v2.jsonl) |
| Coverage | [AO-1 matrix](ao-1-test-matrix-v2.md) |
| Scope | Offline synthetic cases only; no app implementation or runtime dispatch |

## Decision boundary

This candidate incorporates the R1–R10 advisory review findings and two parallel support work products: event/schema/fixture and product/accessibility matrix. Supporting agents worked on separate files; they are not Orchestrator identity dispatches, ACKs, receipts, or human approval. A later independent advisory static review found additional issues; see [AO-1 review report 02](ao-1-review-2026-10-22-02.md). Candidate 2 has not been accepted, schema-validated, replayed, benchmarked, or tested.

Candidate 1 and its review report remain historical. Candidate 2 is submitted for independent document review. AO-2 remains blocked until this packet is accepted, an implementation owner/codebase/capacity/budget are selected, and a separate AO-2 task is approved. Do not validate or execute the fixture until applicable R4a is reviewed, accepted, and frozen with exact inputs/oracle/environment/cap/authority. An independent R4b review must inspect raw evidence after any authorized attempt.

## Scenario set

All events are invented and marked `SIMULATED`. No network, model/provider, target, REA/IDA, W4, training, live agent, command broker, external side effect, private chain-of-thought, credentials, or real transcript is involved. Synthetic budget units are illustrative fixture values, not approved runtime budgets, pricing, or actual costs.

### C01 — parallel work and bounded dissent

Triage-Sentinel works on `TASK-TRIAGE-17` while Product-Evolution-Architect works on `TASK-PRODUCT-08`; assignment and working are separate events. Prompt-Master is invited, accepts and joins before submitting claim `CLM-01`. Evidence-Synthesizer is separately invited, accepts and joins before objecting that `CLM-01` lacks a source locator. Product-Evolution-Architect is invited and defers; its current task remains working at the desk. Synthesis retains the dissent and unresolved source question, then the meeting closes at the two-turn limit without approval, gate movement, or DAG mutation.

The operator should be able to identify the two parallel tasks, who deferred, who joined, which claim is unsupported, whether consensus exists, and why the meeting stopped.

### C02 — cancellation

A separate synthetic meeting proposes, invites, accepts and joins a participant, then is cancelled before synthesis. Cancellation records reason and last turn. It does not imply synthesis, completion, approval, or return movement; location changes only with a later explicit return event.

### C03 — budget stop

A separate synthetic meeting closes with `stop_reason=budget_limit` when its illustrative usage equals its illustrative cap. It is distinct from C01's turn-limit close and does not imply consensus, completion, approval, or real cost.

## Event and replay semantics

The v2 schema is the candidate envelope. It versions the event shape, constrains cases, requires event ID/sequence/time/type, simulation label, source revision and synthetic provenance, and restricts roster and agent references to the six canonical identities. The fixture preserves arrival order; sequence is a separate producer field.

1. Exact byte/content-identical duplicate IDs are idempotent. Same ID with conflicting content is `ID_CONTENT_CONFLICT`, quarantined and diagnosed, with no state mutation.
2. Preserve arrival order and sequence. C01 has arrival sequences `1–17, 19, 20, 18, 22`: late `seq=18` fills the provisional gap after `seq=20`; `seq=21` remains an end-of-stream gap. Keep the inversion diagnostic and never roll back latest state.
3. Stale and heartbeat events change presence only. A late lower-sequence heartbeat cannot overwrite a higher-sequence stale state.
4. Assignment and working are distinct. Invite, accept, defer, join, contribution, cancel and close are separate states. Contribution authors must have joined; deferral preserves existing work.
5. Empty evidence refs render `NO_EVIDENCE_REF`. Synthesis preserves unsupported claims, objections, dissent and open questions. A decision candidate never becomes approval, receipt, gate transition, or DAG mutation.
6. Cancellation is not completion. `turn_limit` and `budget_limit` remain distinct stop reasons.
7. Unknown event/schema versions show unsupported state and cannot produce success.

## Expected-state crosswalk

Detailed case-to-predicate mapping and hard failures are in [AO-1 matrix v2](ao-1-test-matrix-v2.md). Key event locators in the authored fixture:

| Case | Event locator | Expected state |
|---|---|---|
| C01 parallel work | `evt-002`–`evt-005` | Two separately assigned tasks progress to working; neither is overwritten. |
| C01 participation | `evt-007`–`evt-015` | Prompt-Master and Evidence-Synthesizer each have invite→accept→join; Product-Evolution-Architect invite→defer leaves its task intact. `evt-014` is repeated exactly once as the idempotency stimulus. |
| C01 claim/dissent | `evt-016`–`evt-018` | Joined authors only; `CLM-01` has no evidence ref; objection links to claim; synthesis preserves dissent and `HOLD_FOR_EVIDENCE`. |
| C01 ordering/stop | `evt-018`–`evt-021` | Arrival inversion is visible; late seq 18 closes provisional gap; final seq 21 remains open; stale state is not overwritten by older heartbeat. Close is due to turn limit. |
| C02 cancellation | `evt-101`–`evt-106` | Cancel before synthesis; no completion or unlogged movement. |
| C03 budget stop | `evt-201`–`evt-203` | Synthetic usage equals synthetic cap; reason is budget limit and remains distinct from turn limit. |

No verdict is `PASS` from authored data alone. All acceptance and matrix rows remain `OPEN / NOT_RUN` pending review and, where applicable, later frozen execution evidence.

## Visual storyboard, accessibility and privacy

Keep the “observation room” visual direction: small isometric office with six canonical identities, desks and one meeting room; timeline and structured panels remain the precise information surface. Persistent `SIMULATED · OFFLINE` is visible in header and details. Only event-backed transitions move avatars. Timeline includes arrival order, sequence, event ID, actor, task/meeting and anomaly labels. Joined attendees are separated from deferred invites. Claim and objection cards link by ID; absent evidence is explicit. Synthesis separates agreements, dissent, unsupported claims, questions, candidate and stop reason. A 2D roster/table and timeline expose equivalent information.

Accessibility predicates stay open until evidence shows: keyboard-only operation of controls/roster/timeline/details; visible focus and announced identity/event/current row; zoom reset and keyboard alternatives; reduced motion removes travel while preserving state/event cues; 2D fallback exposes equivalent task/meeting/evidence/dissent/stop information; all color status also has text and icon/shape. Screen-reader labels and focus order receive independent inspection.

Fixture contains synthetic identifiers and statements only; no personal data, private chain-of-thought, hidden prompt, credentials, source contents, target identifier or real transcript. Local evidence references remain inert. Missing/invalid provenance cannot become supported through synthesis or visual styling. Any later live-data use requires separate access, rights, redaction, retention, export/delete and threat review.

## Acceptance set

Candidate predicates: `AO1-SCOPE-01`, `AO1-ID-01`, `AO1-SCHEMA-01`, `AO1-STATE-01`, `AO1-PARALLEL-01`, `AO1-INVITE-01`, `AO1-MEETING-01`, `AO1-LINEAGE-01`, `AO1-DISSENT-01`, `AO1-REPLAY-01`, `AO1-CANCEL-01`, `AO1-STOP-01`, `AO1-BUDGET-01`, `AO1-A11Y-01`, `AO1-PRIV-01`, `AO1-R4-01`. Full observables and hard failures are in the matrix. All remain `OPEN`; execution is `NOT_RUN`.

Hard failures cannot be averaged away. Schema/reducer correctness, visual judgment, accessibility, and AO-4 UX value remain separate. These predicates do not alter R0–R6, W0–W7, G1–G4, P1 or W4.

## Review request and missing decisions

Request independent document review of this exact revision, schema, fixture and matrix. Reviewers should record `PASS/FAIL/OPEN` with locators and preserve dissent. Review is not acceptance. Only the coordinator may accept this packet or authorize a separate AO-2 task.

AO-2 owner, app codebase, capacity, browser target, technology, numeric implementation budget and authority remain unselected. No AO-2 task is dispatched here.

## Provenance and inherited gate snapshot

Inputs read directly for this continuation: workspace `START_HERE.md`, workspace map, package `AGENTS.md`, current context, phase map, work queue, six-identity architecture; proposal roadmap, architecture, runbook, verification plan, visual review, preflight/benchmark guidance, AI_Judges review, context handoff, AO-1 review report 01 and support coordination report. The two new v2 artifacts were authored by parallel support agents on separate files and integrated into this candidate. No archive, target, provider, runtime or source code was used.

Preserve: P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`. Six identities, REA–IDA boundaries, all phase/gate systems and historical FAIL are unchanged. This packet creates no ACK, receipt, permission, target pair, runtime capability or gate evidence.
