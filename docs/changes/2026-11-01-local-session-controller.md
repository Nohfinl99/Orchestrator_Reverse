# Local session controller M0–M3

Added `scripts/session_task.py` and `orchestrator_session/` for a bounded document-only local task lifecycle. Commands create a task, prepare an attempt/work packet, record result/review files, and check/report bindings. The existing `orchestrator_pipeline` caller, archived control plane, frozen instructions, role identities and global gate views remain unchanged.

The controller preserves exact original/request bytes, pins sources/context, binds task/attempt/result/review digests, rejects stale output and prevents record overwrite. It checks caller-provided coverage mechanically; `full_completion` and authenticated acceptance remain false. Root's actual semantic review remains outside this unauthenticated local record mechanism. No model/tool dispatch, provider/native execution or consumer KB admission is implemented.

## Verification performed

- The final logic revision ran 14 unittest methods on Windows: 12 passed; 2 symlink tests skipped because the host lacked link-creation privileges. CLI lifecycle, stale bindings, missing evidence, no self-authentication, immutable records, partial publication and public output path rejection were exercised. Direct SUBST-drive behavior was not set up or tested; resolved-ancestry source repair received independent static review.
- Initial execution failed because hard-link publication was denied by the sandbox. The Windows branch now uses exclusive rename, while POSIX uses exclusive hard links. Two path findings were corrected: public path aliases and unsafe task-level attempts enumeration. Original failure and review records were retained locally.
- A real session worker edited one title in a sample README through a prepared packet. Root independently checked the exact byte replacement and CRLF preservation, observed `PENDING_REVIEW` before review, and recorded its review. The final CLI report remained `REVIEW_RECORDED_UNVERIFIED`, with no authenticated/full-completion claim.

This evidence supports only the new local file lifecycle and the bounded sample task. It does not close G1–G4/W4, prove an autonomous six-agent runtime, authenticate an arbitrary imported review, or validate upstream native tools. Point-in-time path checks are not an OS sandbox or a defense against hostile concurrent filesystem changes.

Local evidence is at `evidence/orchestrator_meetings/20261101_session_controller_01/` in the parent workspace and is not included in public clones. See [usage and limits](../operations/local-session-controller.md).
