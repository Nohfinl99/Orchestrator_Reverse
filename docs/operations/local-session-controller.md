# Local session controller

This is a file-only lifecycle helper for one local task. It records the request, creates immutable attempts and work packets, accepts operator-selected result/review files, and checks their bindings mechanically. It does not start an agent, call a model/provider, select a skill, invoke tools, or dispatch work. Output storage must be chosen explicitly outside the public repository.

## Commands

Run from the public package root with isolated Python:

On this Windows workspace use `py -3.14` instead of `python` if the latter is an unconfigured WindowsApps alias. All CLI data output is UTF-8 JSON.

```powershell
python -I -B scripts/session_task.py --help
python -I -B scripts/session_task.py create --request C:\work\request.json --output-root C:\work\sessions
python -I -B scripts/session_task.py prepare-work --task-dir C:\work\sessions\TASK --attempt-id attempt-01 --executor UNKNOWN
python -I -B scripts/session_task.py record-result --task-dir C:\work\sessions\TASK --attempt-id attempt-01 --result C:\work\result.json
python -I -B scripts/session_task.py check --task-dir C:\work\sessions\TASK --attempt-id attempt-01
python -I -B scripts/session_task.py record-review --task-dir C:\work\sessions\TASK --attempt-id attempt-01 --review C:\work\review.json
python -I -B scripts/session_task.py report --task-dir C:\work\sessions\TASK --attempt-id attempt-01
```

The request is UTF-8 JSON with schema `orchestrator.session-request.v1`. It carries `task_id`, original request path/encoding, objective, scope, decision provenance, one of the six existing owners, acceptance rows (`id`, `description`, `required`), input/context pins (`id`, `path`, `revision`), selected/rejected skills, dependencies, output contract, and stop limits. Referenced paths are relative to the request file. `create` preserves the exact request and original bytes and pins input/context bytes.

The work directory is created for each attempt. Put declared deliverables at the packet's `work_dir` paths. The result JSON schema is `orchestrator.session-result.v1` with `binding` copied from `packet.json`, `executor`, `claimed_status` (`DONE`, `PARTIAL`, or `BLOCKED`), declared `outputs`, per-criterion records, and `limitations`. `record-result` verifies output paths and digests those files into a receipt. Review JSON schema is `orchestrator.session-review.v1`, bound to the same packet and result digest; it includes reviewer/producer/provenance strings, evidence, criteria, and limitations. These strings are not authenticated identity.

`prepare-work` records the executor as `UNKNOWN` unless the caller supplies an observed label. `--parent-attempt` links history; attempts and records are append-only. Successful `check` and `report` commands return exit code 0 even when state is `PENDING_RESULT` or `PENDING_REVIEW`; invalid/stale records raise an error. `report` always sets `full_completion=false` and semantic acceptance pending independent root review. Inspect JSON output and its `gaps` list; command success indicates only a report was produced.

Without `--attempt-id`, check/report validate the task and pinned sources and list attempts. They do not inspect every attempt's result/review; specify an attempt to validate those records and outputs. Publication uses exclusive rename on Windows and hard links on POSIX; unsupported storage fails, and an incomplete bundle with no final manifest is not a successful record. Path/reparse checks are point-in-time checks, not an OS sandbox or protection against hostile concurrent filesystem changes.

Run the new contract suite from the public root with `python -I -B -m unittest discover -s tests -p test_session_controller.py -v`. Tests use isolated directories under the parent workspace `local-runs`; a host that cannot create symlinks records explicit skips. This suite is for the new local caller, not the historical business fixture or model/native benchmark.

## Interpretation and limits

`check` and `report` include `goal_review`: the preserved original's path/digest/encoding, the caller-declared objective, scope, acceptance rows and decision provenance. These are displayed together so a reviewer can compare the actual request with the task being claimed complete. The acceptance rows are caller declarations, not a verified oracle for the user's request. Even a DONE result with all recorded criteria satisfied retains `alignment=UNVERIFIED_REQUIRES_ROOT_COMPARISON` and `original_goal_resolution=NOT_ESTABLISHED`.

This is a visibility change in the existing CLI, not semantic detection or enforcement. It does not authenticate statements such as “user approved replacement” in provenance. Follow [goal continuity](goal-continuity.md): read the original and latest user decisions, establish the active goal, and distinguish a completed document/branch from the user's goal. No new wrapper is required; persisted v1 request/packet/result/review schemas and receipts retain their behavior.

Checks cover local structure, digest consistency, task/attempt/input/context/output binding, and acceptance-criterion coverage. They do not decide whether the work satisfies the original request. Review content and reviewer identity are caller-supplied data: the recorded reviewer origin is unauthenticated, and a claimed `PASS` does not establish trusted acceptance or authorize downstream work. A semantic review by the actual Orchestrator/root must inspect the original request, sources, artifact, and review evidence independently. Until that review exists, the task remains pending root review. No local result changes project-wide gates, identities, or runtime state.

Paths and JSON files are data, not instructions to execute. Keep task storage in a dedicated local output directory and provide each input explicitly; the controller does not scan the workspace or execute payloads.
