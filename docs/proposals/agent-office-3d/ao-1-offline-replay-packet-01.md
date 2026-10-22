# AO-1 offline replay packet

| Field | Value |
|---|---|
| Packet ID | `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01` |
| Revision | `1-candidate` |
| Date | 2026-10-22 |
| Roadmap | `AGENT_OFFICE_PRODUCT_ROADMAP_01` rev 1 |
| Status | `REVIEWED_ADVISORY / REVISE_NOT_ACCEPTED / NOT_RUN` |
| Candidate artifacts | [event schema](ao-1-event.schema.json), [synthetic fixture](ao-1-fixture.jsonl), this scenario/oracle/storyboard |
| Scope | One deterministic, offline meeting replay; no app implementation or runtime dispatch |

## Decision boundary

This packet is a review candidate with advisory review findings recorded in [AO-1 review report](ao-1-review-2026-10-22-01.md). It does not dispatch an Orchestrator identity, accept the product packet, authorize AO-2, or change any project gate. AO-2 remains blocked until independent review findings are resolved, a separate implementation owner/codebase/capacity and budget are selected, applicable R4a is accepted/frozen before any execution, and the human coordinator accepts a specific AO-2 task.

The fixture is authored synthetic data, not execution evidence. The schema file's JSON syntax was checked, but the fixture has **not** been validated against the schema, replayed, benchmarked, or tested. Do not execute/validate it until a separate applicable R4a record freezes the candidate/schema/fixture/oracle/environment/cap/authority, followed by an authorized bounded attempt and independent R4b review of raw evidence. R4a/R4b are benchmark controls, not a claim that AO-1 itself has passed.

## Scenario: blocked task, deferred reviewer, bounded dissent meeting

**Operator and question.** An Orchestrator operator is reviewing a proposed offline workflow change. Triage-Sentinel is already working on `TASK-TRIAGE-17`. Prompt-Master has a synthetic structured claim that a proposed workflow is compatible; Evidence-Synthesizer is invited to review its provenance and challenges the claim because its cited source locator is missing. Product-Evolution-Architect is invited but busy and defers; its existing work must continue. A two-round, synthetic meeting closes at its configured turn limit with unresolved dissent. The decision candidate is explicitly not approval, gate movement, or DAG mutation.

**User task.** From one replay, identify (1) who is busy/deferred, (2) who actually joined, (3) which claim lacks evidence, (4) whether the meeting reached consensus, and (5) why it stopped. The 3D scene is an overview; event timeline and structured panels are authoritative for the display.

**Synthetic identities.** The roster contains exactly the six existing identities: Prompt-Master, Triage-Sentinel, Decomp-Analyst, Crypto-Logic-Specialist, Evidence-Synthesizer, Product-Evolution-Architect. This fixture changes location/activity only for Evidence-Synthesizer after join and submitted contribution/objection events. The other identities remain at their desks; no synthetic identity is an actual invocation.

**Limits.** `SIMULATED`; offline; no network, model/provider, target, REA/IDA, W4, training, live agent, command broker, or side effect. Two meeting turns maximum; synthetic budget ceiling 100 units; fixture reports 68 units consumed. These are scenario values, not runtime budgets, pricing, or approved caps. No private chain-of-thought, hidden prompts, credentials, or unscopeable context is present.

## Event contract candidate

The adjacent JSON Schema is the normative envelope candidate for this packet. Each JSONL line is one append-only event. Required fields bind schema version, scenario, event identity/sequence/time/type, simulation label, source revision, and provenance. Entity references and payload fields are typed. `source_revision` identifies this packet fixture, not an Orchestrator runtime revision. Evidence refs are locators; an empty list means no evidence reference is supplied and must render as `NO_EVIDENCE_REF`, never as evidence-backed.

Reducer rules proposed for review:

1. Deduplicate by `event_id`; repeated IDs are idempotent and do not repeat an action.
2. Preserve arrival order separately from `seq`. A lower sequence or sequence gap raises a visible ordering/gap condition; it must not roll back a newer known state or be silently repaired.
3. A heartbeat timeout marks presence `stale`; lack of heartbeat never implies complete, failed, or live.
4. `meeting.invited`, `meeting.deferred`, `meeting.accepted`, and `meeting.joined` are distinct. Only `joined` places a participant in the meeting; deferred/busy work and desk location remain intact.
5. A contribution/objection must reference its meeting and author. Evidence absence remains explicit. Synthesis may list a decision candidate but cannot erase unresolved dissent or create approval/receipt/gate/DAG change.
6. `meeting.closed` records a stop reason and final turn. A turn/budget stop is not task completion.
7. Unknown event types or unsupported schema versions produce a visible `unknown/unsupported` condition and no success transition.

### Vocabulary and state projection

Keep `work_status`, `location`, `presence`, and per-meeting `participant_status` as separate axes. Initial scenario state is fixture-derived: Triage-Sentinel `working/desk/live`; Product-Evolution-Architect `working/desk/live`; Evidence-Synthesizer `available/desk/live`; remaining identities `idle/desk/live`. These are synthetic setup values, not assertions about live agent status. The event log contains only changes relevant to this scenario; a roster seed is presentation metadata and does not imply runtime presence.

## Fixture and expected-state oracle

Fixture path: [ao-1-fixture.jsonl](ao-1-fixture.jsonl). It contains one intentional duplicate (`evt-006`), one sequence inversion (`seq=9` follows `seq=12` in arrival order), a gap (`seq=13` absent), and a heartbeat timeout represented by `presence.stale`. These are test stimuli, not accidental corruption. Fixture order is significant and must not be sorted before a future run.

| Checkpoint / event | Expected visible state | Hard failure |
|---|---|---|
| Seed / `evt-001` | Six named identities; all labeled `SIMULATED`; task `TASK-TRIAGE-17` remains assigned and working at desk. | Missing/extra identity; simulation badge absent; office animation implies unlogged work. |
| `evt-003` invite | Evidence-Synthesizer invited, still at desk until joined. Product-Evolution-Architect has an invite pending. | Invite displayed as accepted or avatar moved into room. |
| `evt-004` defer | Product-Evolution-Architect `deferred`, remains working at desk on its existing task. | Task preempted, hidden, or participant shown in meeting. |
| `evt-005` accept / `evt-006` join | Evidence-Synthesizer accepted then joined; only it is in meeting. | Accepted and joined collapsed into one unsupported state; deferred participant counted as attendee. |
| `evt-007` contribution | Claim `CLM-01` is attributed to Prompt-Master; evidence refs empty, rendered `NO_EVIDENCE_REF`. | Claim appears sourced/verified or author unclear. |
| duplicate `evt-006` | No second join action, motion, or participant count increment; duplicate diagnostic visible. | Non-idempotent effect. |
| `evt-009`, `evt-010` objection | Objection `OBJ-01` links to `CLM-01`; unresolved dissent retained. | Objection detached from claim or omitted from minutes. |
| `evt-011` synthesis | Agreements empty; dissent contains both claim and objection; unsupported claim includes `CLM-01`; open question retained; `decision_candidate=HOLD_FOR_EVIDENCE`; approval false. | Consensus inferred; dissent dropped; candidate rendered as approved/accepted or gate/DAG mutation. |
| sequence inversion and gap | Show ordering warning for arrival inversion and missing sequence 13; preserve latest state and raw event order. | Silent reorder, state rollback, or hidden gap. |
| `evt-012` stale | Evidence-Synthesizer presence is `stale`; meeting/work facts remain unchanged. | Stale converted to failure/completion or hidden. |
| `evt-013` close | Meeting closed at turn 2, stop reason `turn_limit`; synthetic budget 68/100; no approval or task completion. | Turn stop treated as consensus, task completion, or budget exceeded. |

The event's `seq` is producer sequence. For this fixture `evt-012` deliberately has sequence 9 after sequence 12; consumers preserve source arrival order and surface the anomaly. Missing sequence 13 is an explicit gap between 12 and 14. No wall-clock timing or nondeterministic animation is part of the oracle.

## Visual storyboard and 2D fallback

1. **Replay header:** persistent `SIMULATED · OFFLINE` badge, scenario name, play/pause/step/replay controls, and a static note that this is not a live Orchestrator session.
2. **Spatial overview:** small isometric room, six-person roster, desks and one meeting room. Default positions are roster seed only. Event-linked location changes are short and deterministic; deferred Product-Evolution-Architect stays at the desk with `DEFERRED` text/icon.
3. **Event timeline:** fixed-width readable event rows with arrival index, `seq`, event ID, actor, task/meeting, and warning chips for duplicate/order/gap/stale. Selecting a row drives the same reducer state as the scene.
4. **Meeting panel:** attendee list includes only Evidence-Synthesizer as joined; deferred invite appears separately. Contribution and objection are separate cards with links to claim IDs. Empty evidence is shown as `NO_EVIDENCE_REF`.
5. **Synthesis panel:** separate agreements, dissent, unsupported claims, open questions, candidate, stop reason and synthetic budget. Show `NOT APPROVED`; do not use a green success treatment for the candidate.
6. **2D equivalent:** keyboard-operable roster/table and timeline expose every location/status/participant/claim field without requiring spatial navigation. Reduced-motion mode removes travel/cues while preserving event highlighting and all labels.

Motion and color are redundant cues only. Every state has text and an icon/shape; status is never encoded by color alone. Keyboard focus order is header controls → roster → timeline → detail panels; selected identity/event is announced with a readable label. Zoom/pan has reset and keyboard alternatives.

## Privacy, security, and provenance

- Fixture data is synthetic and contains no personal data, real transcript, source contents, credentials, target identifiers, or private reasoning.
- Render only submitted structured output and explicit evidence locators. Never infer, request, or display private chain-of-thought.
- Links remain inert local references in AO-1. Any future live data requires a separate access, rights, redaction, retention, export/delete, and threat review before ingestion.
- `SIMULATED` is required on every event and persistent in every view; no simulated receipt is represented as a real authority receipt.
- Missing/invalid provenance is visible and cannot be upgraded to a supported claim by synthesis or styling.

## Acceptance predicates

These are candidate AO-1/AO-2 packet predicates, not project gates and not run results. `PASS` requires exact review locator/evidence; currently every predicate is `OPEN` pending independent review and, where applicable, implementation/evaluation.

| ID | Predicate | Evidence required for a future verdict |
|---|---|---|
| `AO1-SCOPE-01` | Scenario is offline and synthetic; no runtime/provider/target/REA/IDA/W4/training call or side effect. | Reviewed scope and later attempt environment/raw record. |
| `AO1-ID-01` | Roster is exactly the six current identities; no identity or alias added. | Schema/fixture inspection and rendered roster capture. |
| `AO1-SCHEMA-01` | Versioned envelope validates required provenance, IDs, event payloads, and simulation label. | Schema review; any execution requires frozen R4a and raw validator output. |
| `AO1-STATE-01` | Work, location, presence, and participant status remain distinct. | Expected-state table and reducer/UI evidence. |
| `AO1-INVITE-01` | Busy/deferred invite does not preempt work or count as attendance. | `evt-004` expected-state and UI capture. |
| `AO1-MEETING-01` | Only accepted+joined participant is shown in room/attendance. | `evt-005`/`evt-006` expected-state and UI capture. |
| `AO1-LINEAGE-01` | Claim/objection preserve author and links; unsupported/missing evidence is explicit. | `CLM-01`/`OBJ-01` panel locator and captured state. |
| `AO1-DISSENT-01` | Synthesis retains unresolved dissent/open question and does not assert consensus/approval. | `evt-011` oracle and rendered minutes. |
| `AO1-REPLAY-01` | Duplicate is idempotent; inversion/gap are visible; replay is deterministic and does not roll back state. | Frozen fixture/candidate and deterministic output comparison from authorized run. |
| `AO1-STOP-01` | Turn/budget stop is visible and is not task completion or approval. | `evt-013` expected-state and rendered capture. |
| `AO1-A11Y-01` | Keyboard, text/icon status, reduced-motion, and usable 2D fallback expose equivalent information. | Independent accessibility review and interaction evidence. |
| `AO1-PRIV-01` | No private reasoning/secrets; simulation and missing provenance remain explicit. | Source review plus UI/data inspection. |
| `AO1-R4-01` | Any benchmark/fixture attempt has accepted R4a before it and independent R4b after raw evidence. | R4a freeze record, bounded raw attempt, separate R4b review. |

Hard failures cannot be averaged away. UI visual judgment, reducer correctness, accessibility, and UX value are separate findings. No threshold for AO-4 user study is set here.

## Review and handoff

**Requested reviewers:** Product-Evolution-Architect for operator task/acceptance; Evidence-Synthesizer independent review for source binding, semantics, missing evidence, and oracle contradictions. These are responsibility mappings, not dispatched identities or ACKs. Record each predicate `PASS/FAIL/OPEN` with locator and preserve dissent. Maximum two document-review rounds per existing guidance; after unresolved findings, mark `REVISE_NOT_ACCEPTED` or `BLOCKED` and create a new candidate revision after edits.

**Human decision:** only the coordinator may record `ACCEPTED` or authorize a separate AO-2 task. Current packet remains `READY_FOR_INDEPENDENT_REVIEW`; AO-2 is `BLOCKED_ON_AO1_ACCEPTANCE`. Missing implementation owner, app codebase, capacity, browser target, numeric AO-2 budget and separate benchmark authority remain `UNKNOWN / NOT_SELECTED`; they are not guessed here.

### Provenance read for this candidate

Read directly: workspace `START_HERE.md`; workspace `docs/ia/workspace-map.md`; package `AGENTS.md`; package `context/current.md`; package `context/handoff.md`; `docs/planning/phase-map.md`; `docs/planning/work-queue.md`; package `docs/architecture/agents.md`; proposal `README.md`, `architecture.md`, `meeting-review-2026-10-22-01.md`, `roadmap.md`, `execution-runbook.md`, `verification-plan.md`, `preflight-knowledge-and-benchmark.md`, `visual-review-2026-10-22-01.md`, `ai-judges-review-2026-10-22-01.md`, and `context-handoff-implementation-2026-10-22.md`. No archive, target, provider, runtime, source fixture, or UI implementation was read or run for this packet.

### Gate snapshot retained

P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`. Six identities, REA–IDA ownership/boundaries, all phase/gate systems, and historical FAIL remain unchanged. AO-1 design does not create G1–G4 evidence, consumer ACK, permission, receipt, or runtime capability.
