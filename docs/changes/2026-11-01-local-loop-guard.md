# M4 local no-progress guard

New opt-in caller: [guide](../operations/local-loop-guard.md), `scripts/loop_guard.py`, `orchestrator_session/loop_guard.py` and `trace_review.py`. It records raw/normalized failures, lineage-wide reserved budgets, current candidate/source bindings, progress-review references and immutable ledger events. Trace inspection separates observed violations from unconfirmed causes.

Existing v1 core, CLI, script and test source are preserved. Explicit selected review remains an unverified caller assertion; a retry candidate grants no authority. Same-lineage changed branch context waits for review, rather than implicitly proving independence. Independent selected lineages can be assessed separately; this is not a full DAG scheduler or global worker-loop controller.

Local execution/review details are retained outside this public repository under workspace run `evidence/orchestrator_meetings/20261101_m4_local_01/`. Public documentation does not distribute those local raw records. No native/provider/cloud/training/W4, identity/gate changes or publication is implied. Global gate states and original protocols remain unchanged.
