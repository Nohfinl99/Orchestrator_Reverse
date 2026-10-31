---
name: orch-d810-ng
description: Guide evidence-led use and review of D-810-ng as an IDA Hex-Rays microcode transformation aid for a bounded deobfuscation question. Use only when a task explicitly concerns D-810 or its microcode rules; this instruction skill does not install or run the plugin.
---

# D-810-ng review workflow

Use D-810-ng as a candidate transformation aid when the target is an IDA database and a specific microcode or control-flow pattern is under review. It is not a universal deobfuscator: a rule can be inapplicable, configuration-dependent, or semantically wrong for the target's assumptions.

## Establish applicability

1. Reuse authorization already given for this same action and scope. Ask only if materially needed target or scope information is missing. Confirm the exact target, IDB, function address/range, architecture, and analysis state. Record hashes or other stable provenance for the input and IDB; distinguish the original from any working copy.
2. Identify the actual IDA and Hex-Rays versions, Python/runtime, D-810 revision, configuration, and enabled rules. The captured README describes IDA 9+ and Python 3.10+; treat this as a claim from that historical snapshot, not a current compatibility guarantee. Check the installed plugin's own metadata and compatibility before use.
3. If the plugin is absent or compatibility is unverified, stop at static review of the supplied evidence. Do not install, fetch, or execute it just because this skill was invoked.
4. State the exact hypothesis: the suspected transformation, relevant control/data-flow, and what observation would falsify it. Keep unrelated functions out of scope.

## Assess a transformation

- Locate the rule and its preconditions, maturity level, project configuration, and any solver or verification exception. The README describes MBA simplification, opaque-predicate and control-flow rules, and rule verification; those labels do not prove that a particular rule applies correctly to this binary.
- Compare the original pseudocode/microcode and CFG with the transformed result. Preserve the rule identity, configuration, function address, microcode maturity, and before/after evidence.
- Check semantic behavior independently: widths, signedness, overflow, flags, memory effects, aliasing, side effects, exceptional paths, and reachability. A symbolic equivalence proof covers only its encoded bit-vector model and assumptions. Record skipped verification and unsupported operations.
- Separate code-view simplification from a byte patch. Do not patch bytes or IDB state unless the user's task explicitly authorizes that operation; keep a reversible copy and preserve original bytes and a diff when patching is authorized.
- Report confirmed equivalence, counterexample, or uncertainty. A cleaner decompilation is not proof of behavior.

## Orchestrator boundaries

Keep REA–IDA ownership with the existing owner and preserve the six project identities. This skill creates no identity, runtime adapter, pair, ACK, or gate status. Small models may search or extract a bounded source slice; use a high-capability reviewer for difficult cases, while the root/owner and independent reviewer decide semantic validity and any state transition under the existing project workflow. Record conflicts as issues rather than changing frozen evidence or historical FAILs.

## References

See [source.md](references/source.md) for the pinned README and evidence limits.
