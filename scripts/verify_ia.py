"""Read/hash/link checks for public IA documents. Never imports project code."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = "metadata/content-manifest.json"
SKIP = {".git", "__pycache__", ".venv", "venv", "node_modules"}


def files():
    return sorted(p for p in ROOT.rglob("*")
                  if p.is_file() and not SKIP.intersection(p.relative_to(ROOT).parts)
                  and p.relative_to(ROOT).as_posix() != INVENTORY)


def row(path):
    data = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def local(name):
    if not isinstance(name, str) or not name or "\\" in name:
        raise ValueError("INVALID_LOCAL_PATH")
    path = (ROOT / name).resolve()
    if PureWindowsPath(name).drive or not path.is_relative_to(ROOT) or path == ROOT:
        raise ValueError("PATH_OUTSIDE_PUBLIC_ROOT:" + name)
    return path


def verify():
    errors = []
    inventory = load(INVENTORY)
    expected = inventory.get("files")
    if inventory.get("schema") != "orchestrator.ia-content.v1" or not isinstance(expected, list) or not expected:
        raise ValueError("EMPTY_OR_INVALID_CONTENT_INVENTORY")
    listed = set()
    for entry in expected:
        name = entry["path"]
        path = local(name)
        if name in listed:
            errors.append("DUPLICATE_PATH:" + name)
        listed.add(name)
        if not path.is_file() or row(path) != entry:
            errors.append("CONTENT_MISMATCH:" + name)
    actual = {p.relative_to(ROOT).as_posix() for p in files()}
    if listed != actual:
        errors.append({"inventory_missing": sorted(actual - listed), "files_missing": sorted(listed - actual)})

    preservation = load("metadata/preservation.json")
    originals = preservation.get("files")
    if preservation.get("schema") != "orchestrator.ia-preservation.v1" or not originals:
        raise ValueError("EMPTY_OR_INVALID_PRESERVATION")
    preserved = relocated = 0
    editable = {"README.md", ".gitattributes"}
    for entry in originals:
        if entry["policy"] == "NAVIGATION_EDIT_ALLOWED":
            if entry["original_path"] not in editable or entry["path"] != entry["original_path"]:
                errors.append("INVALID_EDIT_EXCEPTION:" + entry["original_path"])
            continue
        if entry["policy"] not in ("BYTE_IDENTICAL", "RELOCATED_BYTE_IDENTICAL"):
            errors.append("UNKNOWN_PRESERVATION_POLICY:" + entry["original_path"])
            continue
        path = local(entry["path"])
        if not path.is_file() or row(path) != {k: entry[k] for k in ("path", "bytes", "sha256")}:
            errors.append("ORIGINAL_BYTES_CHANGED:" + entry["path"])
        preserved += 1
        relocated += entry["policy"] == "RELOCATED_BYTE_IDENTICAL"

    link_count = 0
    for page in files():
        if page.suffix.lower() != ".md":
            continue
        for target in re.findall(r"\]\(([^)\n]+)\)", page.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            link_count += 1
            resolved = (page.parent / unquote(target.split("#", 1)[0])).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append({"broken_or_external_local_link": str(page.relative_to(ROOT)), "target": target})
            elif resolved.relative_to(ROOT).as_posix() != (page.parent / unquote(target.split("#", 1)[0])).relative_to(ROOT).as_posix() and ".." not in target:
                errors.append("LINK_CASE_OR_PATH_MISMATCH:" + target)

    nav = load("metadata/navigation.json")
    paths = nav["default_read_order"] + list(nav["canonical"].values())
    paths += [p for route in nav["task_routes"].values() for p in route]
    for name in paths:
        if not local(name).is_file():
            errors.append("NAVIGATION_TARGET_MISSING:" + name)
    for old, new in nav["compatibility_routes"].items():
        if not local(old).is_file() or not local(new).is_file():
            errors.append("REDIRECT_MISSING:" + old)
        elif new.removeprefix("docs/") not in local(old).read_text(encoding="utf-8"):
            errors.append("REDIRECT_WRONG_TARGET:" + old)

    state = load("context/project-state.json")
    gates = {"P1K_B4": "FAIL", "G1": "INCOMPLETE", "G2": "INCOMPLETE", "G3": "NOT_RUN",
             "G4": "NOT_RUN", "W4_runtime": "NOT_RUN_BLOCKED", "v3": "OFF"}
    if {key: state["gates"].get(key) for key in gates} != gates or state["gate_promotion_from_ia"] is not False:
        errors.append("GATE_VIEW_CHANGED")
    w4 = {"W4_readiness_run44": "RECONCILED_BLOCKED_RUNTIME",
          "I01": "INELIGIBLE_G1_G2_G3",
          "I02": "INELIGIBLE_G1_PROVIDER_MODEL_UNRESOLVED",
          "I03": "INELIGIBLE_I02_NUMERIC_BUDGET_UNRESOLVED",
          "I04": "INELIGIBLE_G1_G3",
          "I05": "VERIFIED_NON_TARGET_PREPARATION_RUN43"}
    if any(state["gates"].get(key) != value for key, value in w4.items()):
        errors.append("W4_READINESS_VIEW_CHANGED")
    if state["phase_systems"]["W"] != ["W" + str(n) for n in range(8)] or state["phase_systems"]["R"] != ["R" + str(n) for n in range(7)]:
        errors.append("PHASE_IDENTIFIERS_CHANGED")
    stacks = list((ROOT / "prompt_stacks").glob("[0-9][0-9]_*.md"))
    protocols = list((ROOT / "prompt_stacks/protocols").glob("*.md"))
    frozen_instructions = {e["path"] for e in originals if e["path"].startswith("prompt_stacks/")}
    if len(stacks) != 10 or len(protocols) != 10 or any(p.relative_to(ROOT).as_posix() not in frozen_instructions for p in stacks + protocols):
        errors.append("INSTRUCTION_SET_CHANGED")
    return {"status": "FAIL_IA_CHECKS" if errors else "PASS_IA_DOCUMENT_CHECKS",
            "inventory_files": len(expected), "byte_preserved_files": preserved,
            "relocated_byte_identical": relocated, "local_links_checked": link_count,
            "stacks": len(stacks), "protocols": len(protocols), "errors": errors,
            "scope": "PUBLIC_DOCUMENT_INTEGRITY_AND_NAVIGATION_ONLY",
            "project_workloads_rerun": 0, "runtime_gate_promotion": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", action="store_true", help="Print proposed navigation inventory; does not write files or refresh preservation pins")
    args = parser.parse_args()
    try:
        result = {"schema": "orchestrator.ia-content.v1", "scope": "PUBLIC_DOCUMENT_FILES_EXCEPT_THIS_INVENTORY_AND_GIT_INTERNALS", "files": [row(p) for p in files()]} if args.inventory else verify()
        print(json.dumps(result, ensure_ascii=True, indent=2 if args.inventory else None))
        return 1 if result.get("errors") else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "INVALID_IA_INPUT", "error": str(exc)}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
