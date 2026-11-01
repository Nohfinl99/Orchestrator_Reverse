# Orchestrator Toolkit

This package contains five original, instruction-only workflows for CUA, Strix, D810-ng, MicroSMT, and OLLVM project research. It includes no upstream source code, executable, scanner, IDA plugin, MCP server, or runtime.

## Gọi lại skill đã lưu

Trong workspace Orchestrator, năm skill đã được lưu lâu dài tại `.agents/skills/` và có thể được gọi lại ở các phiên sau trong cùng môi trường; không cần cài lại plugin cho từng task. Khi host hỗ trợ gọi skill bằng tên, dùng `$orch-cua`, `$orch-strix`, `$orch-d810-ng`, `$orch-microsmt` hoặc `$orch-ollvm-research`. Có thể yêu cầu bằng ngôn ngữ tự nhiên, chẳng hạn “dùng orch-cua để thao tác UI” hoặc “dùng orch-microsmt để xem opaque predicate”. Xem từng [SKILL.md](skills/orch-cua/SKILL.md) · [SKILL.md](skills/orch-strix/SKILL.md) · [SKILL.md](skills/orch-d810-ng/SKILL.md) · [SKILL.md](skills/orch-microsmt/SKILL.md) · [SKILL.md](skills/orch-ollvm-research/SKILL.md).

Khi dùng public clone, agent có thể đọc trực tiếp các `SKILL.md` trong repo theo hướng dẫn của [AGENTS.md](../../AGENTS.md), không cần nhập plugin. Máy hoặc tài khoản khác cần có quyền truy cập source và tự thiết lập discovery phù hợp. Việc gọi được hướng dẫn không cung cấp công cụ hay runtime; prerequisite của từng workflow vẫn áp dụng.

## Select a workflow by task

| Task | Skill |
|---|---|
| Operate an application or desktop through an available CUA tool | [orch-cua](skills/orch-cua/SKILL.md) |
| Plan, read results, or conduct an authorized security assessment with Strix | [orch-strix](skills/orch-strix/SKILL.md) |
| Review D810-ng microcode rules or transformations in IDA | [orch-d810-ng](skills/orch-d810-ng/SKILL.md) |
| Analyze opaque predicates with MicroSMT | [orch-microsmt](skills/orch-microsmt/SKILL.md) |
| Find and compare projects in awesome-ollvm | [orch-ollvm-research](skills/orch-ollvm-research/SKILL.md) |

Read only the workflow and source note relevant to the task. A skill name does not add an Orchestrator identity; the project retains its six existing identities and REA–IDA ownership.

## Platform use

`PORTABLE_INSTRUCTIONS.txt` is an instruction overlay for platforms that accept user-provided instructions. From the repository root, `scripts/export_toolkit.py` builds checked plugin/skill ZIPs and Gemini Knowledge text files outside the repository. A Gemini discovery worker reported local discovery, and the current local Codex catalogue exposes metadata for these five skills. Neither observation confirms import into a remote account's plugin catalogue or actual platform runtime behavior. The active host must expose any tool/runtime before a workflow can perform actions; otherwise continue available reading, planning or review and report the execution gap.

## Source notes and availability

Each `references/source.md` records a historical upstream commit; some also record the captured README digest. Notes can contain paths into the original local workspace as provenance locators. Those local evidence files are **LOCAL_ONLY_NOT_DISTRIBUTED** and are not dependencies of this public package; this clone cannot validate their contents. The pins are historical and do not establish upstream freshness or redistribution rights. No upstream code or skill text is copied here.

The workflows preserve the project’s evidence, scope, and authorization boundaries. They do not alter project principles, phases, gates, ACKs, or historical FAIL records. See [toolkit use and portability](../../docs/operations/toolkit.md) and [task execution](../../docs/operations/task-execution.md).
