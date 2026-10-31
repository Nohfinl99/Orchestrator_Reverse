---
name: orch-microsmt
description: Assess a bounded opaque-predicate hypothesis using MicroSMT evidence in an IDA/Hex-Rays context. Use when the task explicitly concerns MicroSMT, backward slicing from jcc/setcc, or SMT lifting of microcode; do not treat it as a general-purpose deobfuscator.
---

# MicroSMT assessment workflow

MicroSMT is described in its captured README as an IDA plugin that slices backward from `jcc`/`setcc`, lifts supported Hex-Rays microcode to Z3 expressions, and solves the resulting condition. The same README calls it pre-alpha, warns that microcode has pitfalls and that the lifter does not implement every instruction, and says it was tested on IDA Pro 9.2. Treat any result as a hypothesis tied to a specific slice and model.

## Bound the question

1. Reuse authorization already given for this same action and scope; ask only if materially needed target or scope information is missing. Confirm target and IDB provenance, architecture, function and exact branch/setcc address. Use a working copy and preserve original hashes/state.
2. Record exact IDA/Hex-Rays build, MicroSMT revision, Z3 version, plugin configuration, and whether patching is enabled. Verify compatibility against the actual artifact and host. A historical README test claim is not compatibility proof.
3. Do not install or run the plugin as an automatic consequence of this skill. If unavailable or unverified, analyze only supplied static evidence and label the solver outcome UNKNOWN.
4. Write the predicate hypothesis and assumptions before interpreting a solver result. Capture the backward slice and list unsupported or approximated operations, widths, flags, and path constraints.

## Validate the result

- Distinguish satisfiable, unsatisfiable, timeout/unknown, unsupported lifting, and tool error. A solver answer is meaningful only for the expression actually lifted and its assumptions.
- Independently check bit widths, signedness, overflow, flags, memory and side effects, control-flow reachability, and any omitted state. Seek a concrete counterexample or confirm the equivalence with an independent method appropriate to the claim.
- Preserve the pre-change bytes/IDB, exact address, slice, lifted expression or solver evidence, settings, and before/after CFG. Record uncertainty and unsupported instruction coverage.
- The README describes optional patching of a `jcc` or `setcc`; patch only with explicit task authorization. Keep a reversible working copy, byte diff, and independent post-patch review. Never infer safety from a single `unsat` result.

## Orchestrator boundaries

Maintain existing REA–IDA ownership and six identities. This skill does not establish a connected pair, runtime integration, ACK, or gate promotion. Small models may perform bounded source search or extraction to enumerate the slice; use a high-capability reviewer for difficult semantic questions. Acceptance belongs to the existing owner/root and independent reviewer. Keep historical failures and frozen evidence intact; log conflicts as issues.

## References

See [source.md](references/source.md) for the exact source revision and scope.
