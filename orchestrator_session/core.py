"""Bounded local artifact lifecycle. No dispatch, authenticated review or sandbox."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import uuid

MAX_FILE = 8 * 1024 * 1024
MAX_JSON = 1024 * 1024
ROLES = {"Prompt-Master", "Triage-Sentinel", "Decomp-Analyst",
         "Crypto-Logic-Specialist", "Evidence-Synthesizer", "Product-Evolution-Architect"}
PUBLIC_ROOT = Path(__file__).resolve().parents[1]


class SessionError(ValueError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def require(ok, code, message):
    if not ok:
        raise SessionError(code, message)


def packed(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "INVALID_JSON", "Duplicate JSON member")
        result[key] = value
    return result


def _constant(value):
    raise SessionError("INVALID_JSON", "Nonfinite JSON value")


def decode(raw):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_constant)
    except (UnicodeError, ValueError, RecursionError) as exc:
        if isinstance(exc, SessionError):
            raise
        raise SessionError("INVALID_JSON", str(exc)) from exc


def _shape(value, keys):
    require(type(value) is dict and set(value) == set(keys.split()),
            "INVALID_SCHEMA", "Expected exactly these fields: " + keys)


def _text(value):
    require(type(value) is str and 0 < len(value.strip()) <= 65536,
            "INVALID_SCHEMA", "Expected nonempty bounded text")


def _identifier(value):
    require(type(value) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", value),
            "INVALID_IDENTIFIER", "Expected 1..64 ASCII letters/digits/_/-")
    require(value.upper() not in {"CON", "PRN", "AUX", "NUL", "CONIN", "CONOUT",
            *[f"COM{i}" for i in range(1, 10)], *[f"LPT{i}" for i in range(1, 10)]},
            "INVALID_IDENTIFIER", "Reserved device name")
    return value


def _rows(value):
    require(type(value) is list and len(value) <= 64, "INVALID_SCHEMA", "Expected list of at most64 items")
    return value


def _unique(rows):
    identifiers = [_identifier(row.get("id")) if type(row) is dict else _identifier(None) for row in rows]
    require(len(identifiers) == len(set(identifiers)), "INVALID_SCHEMA", "Duplicate IDs")
    return set(identifiers)


def _safe(path):
    path = Path(os.path.abspath(path))
    for node in (path, *path.parents):
        if os.path.lexists(node):
            stat = node.lstat()
            require(not node.is_symlink() and not (getattr(stat, "st_file_attributes", 0) & 1024),
                    "UNSAFE_PATH", "Symlink/reparse path rejected: " + str(node))
    return path


def _external(path):
    path = _safe(path)
    require(path != PUBLIC_ROOT and PUBLIC_ROOT not in path.parents,
            "OUTPUT_BOUNDARY", "Session output must be outside public repository")
    # Windows extended-length prefixes, DOS short names and drive aliases can
    # spell the same directory differently. A SUBST drive may start inside the
    # public tree, so its lexical ancestors need not include the public root.
    # Resolve the longest existing physical ancestry, including a missing tail,
    # and compare both spellings by identity before creating anything.
    try:
        physical = _safe(path.resolve(strict=False))
    except (OSError, RuntimeError) as exc:
        raise SessionError("IO_ERROR", str(exc)) from exc
    for spelling in (path, physical):
        for node in (spelling, *spelling.parents):
            if os.path.lexists(node):
                try:
                    in_public = os.path.samefile(node, PUBLIC_ROOT)
                except OSError as exc:
                    raise SessionError("IO_ERROR", str(exc)) from exc
                require(not in_public, "OUTPUT_BOUNDARY", "Output aliases public repository")
    return path


def _relative(value):
    _text(value)
    require("\\" not in value and ":" not in value and not value.startswith("/"),
            "UNSAFE_PATH", "Output path must be relative POSIX path")
    parts = value.split("/")
    require(all(part not in ("", ".", "..") and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", part)
                and not part.endswith((".", " ")) for part in parts), "UNSAFE_PATH", "Unsafe output path")
    for part in parts:
        _identifier(part.split(".")[0])
    return str(PurePosixPath(value))


def _read(path, limit=MAX_FILE):
    path = _safe(path)
    try:
        require(path.is_file(), "INPUT_UNAVAILABLE", "Expected regular file: " + str(path))
        require(path.stat().st_size <= limit, "BYTE_BUDGET", "File exceeds byte cap")
        with path.open("rb") as stream:
            raw = stream.read(limit + 1)
        require(len(raw) <= limit, "BYTE_BUDGET", "File grew beyond byte cap")
        return raw
    except OSError as exc:
        raise SessionError("IO_ERROR", str(exc)) from exc


def _atomic(path, raw):
    path = _safe(path)
    temp = path.parent / (".write-" + uuid.uuid4().hex)
    try:
        require(not os.path.lexists(path), "OUTPUT_EXISTS", "Immutable file already exists")
        with temp.open("xb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        # Windows rename is exclusive (FileExistsError if destination exists).
        # POSIX rename may replace, so use exclusive hard-link publication there.
        # Never fall back to os.replace or a check-then-overwriting rename.
        if os.name == "nt":
            os.rename(temp, path)
        else:
            os.link(temp, path)
        require(_read(path) == raw, "INTEGRITY_MISMATCH", "Write readback mismatch")
    except OSError as exc:
        raise SessionError("IO_ERROR", str(exc)) from exc
    finally:
        if temp.exists():
            temp.unlink()


def _mkdir(path):
    path = _safe(path)
    try:
        path.mkdir()
    except FileExistsError as exc:
        raise SessionError("OUTPUT_EXISTS", "Immutable directory already exists: " + str(path)) from exc
    except OSError as exc:
        raise SessionError("IO_ERROR", str(exc)) from exc
    return path


def _commit(directory, files):
    entries = {}
    for name, raw in files.items():
        _atomic(directory / name, raw)
        entries[name] = {"sha256": sha(raw), "bytes": len(raw)}
    manifest = {"schema": "orchestrator.session-manifest.v1", "files": entries}
    raw = packed(manifest)
    _atomic(directory / "manifest.json", raw)
    return sha(raw)


def _bundle(directory, names):
    raw = _read(directory / "manifest.json", MAX_JSON)
    manifest = decode(raw)
    _shape(manifest, "schema files")
    require(manifest["schema"] == "orchestrator.session-manifest.v1", "INVALID_SCHEMA", "Manifest schema")
    require(type(manifest["files"]) is dict and set(manifest["files"]) == set(names),
            "INVALID_SCHEMA", "Manifest file set")
    values = {}
    for name, row in manifest["files"].items():
        _shape(row, "sha256 bytes")
        data = _read(directory / name)
        require(type(row["bytes"]) is int and row["bytes"] == len(data) and row["sha256"] == sha(data),
                "INTEGRITY_MISMATCH", "Stored file changed: " + name)
        values[name] = data
    return values, sha(raw)


def _validate_request(request):
    _shape(request, "schema task_id original objective scope decision_provenance owner acceptance inputs context selected_skills rejected_skills dependencies output_contract stop")
    require(request["schema"] == "orchestrator.session-request.v1", "INVALID_SCHEMA", "Request schema")
    _identifier(request["task_id"])
    _shape(request["original"], "path encoding")
    for key in ("path", "encoding"):
        _text(request["original"][key])
    for key in ("objective", "scope", "decision_provenance"):
        _text(request[key])
    require(type(request["owner"]) is str and request["owner"] in ROLES,
            "INVALID_SCHEMA", "Owner must be one of six identities")
    for key in ("acceptance", "inputs", "context", "selected_skills", "rejected_skills", "dependencies", "output_contract"):
        _unique(_rows(request[key]))
    require(request["acceptance"] and request["output_contract"], "INVALID_SCHEMA", "Need acceptance and output contract")
    for row in request["acceptance"]:
        _shape(row, "id description required")
        _text(row["description"])
        require(type(row["required"]) is bool, "INVALID_SCHEMA", "required must be boolean")
    for key in ("inputs", "context"):
        for row in request[key]:
            _shape(row, "id path revision")
            _text(row["path"])
            _text(row["revision"])
    contexts = {row["id"] for row in request["context"]}
    for row in request["selected_skills"]:
        _shape(row, "id reason context_id")
        _text(row["reason"])
        require(type(row["context_id"]) is str and row["context_id"] in contexts,
                "INVALID_SCHEMA", "Selected skill requires pinned context")
    for row in request["rejected_skills"]:
        _shape(row, "id reason")
        _text(row["reason"])
    require(not ({row["id"] for row in request["selected_skills"]}
                 & {row["id"] for row in request["rejected_skills"]}),
            "INVALID_SCHEMA", "Skill cannot be both selected and rejected")
    for row in request["dependencies"]:
        _shape(row, "id status reason required")
        require(row["status"] in ("READY", "BLOCKED") and type(row["required"]) is bool,
                "INVALID_SCHEMA", "Dependency status/required")
        _text(row["reason"])
    paths = []
    for row in request["output_contract"]:
        _shape(row, "id path required")
        paths.append(_relative(row["path"]).casefold())
        require(type(row["required"]) is bool, "INVALID_SCHEMA", "required must be boolean")
    require(len(paths) == len(set(paths)), "INVALID_SCHEMA", "Duplicate output paths")
    _shape(request["stop"], "max_attempts max_output_bytes note")
    for key, cap in (("max_attempts", 100), ("max_output_bytes", MAX_FILE)):
        require(type(request["stop"][key]) is int and 1 <= request["stop"][key] <= cap,
                "INVALID_SCHEMA", "Stop bound out of range")
    _text(request["stop"]["note"])
    return request


def _pin(path, **metadata):
    path = _safe(path)
    raw = _read(path)
    return {**metadata, "path": str(path), "bytes": len(raw), "sha256": sha(raw)}


def _revalidate(pin):
    raw = _read(pin["path"])
    require(sha(raw) == pin["sha256"] and len(raw) == pin["bytes"],
            "STALE_SOURCE", "Source changed: " + pin["path"])


def create(request_file, output_root):
    request_file = _safe(request_file)
    raw = _read(request_file, MAX_JSON)
    request = _validate_request(decode(raw))
    base = request_file.parent
    original = _pin(base / request["original"]["path"], encoding=request["original"]["encoding"])
    original_raw = _read(original["path"])
    try:
        original_raw.decode(original["encoding"])
    except (UnicodeError, LookupError) as exc:
        raise SessionError("INVALID_ENCODING", str(exc)) from exc
    pins = {key: [_pin(base / row["path"], id=row["id"], revision=row["revision"]) for row in request[key]]
            for key in ("inputs", "context")}
    require(sha(original_raw) == original["sha256"], "STALE_SOURCE", "Original changed while reading")
    task = {"schema": "orchestrator.session-task.v1", "request": request, "original": original,
            "request_source": {"path": str(request_file), "sha256": sha(raw), "bytes": len(raw)}, **pins}
    root = _external(output_root)
    try:
        root.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise SessionError("IO_ERROR", str(exc)) from exc
    directory = _mkdir(root / request["task_id"])
    _mkdir(directory / "attempts")
    task_hash = _commit(directory, {"task.json": packed(task), "original.bin": original_raw,
                                     "request-source.bin": raw})
    return {"status": "CREATED", "task_id": request["task_id"], "task_dir": str(directory),
            "task_sha256": task_hash, "authenticated_acceptance": False}


def _task(task_dir):
    directory = _external(task_dir)
    files, digest = _bundle(directory, {"task.json", "original.bin", "request-source.bin"})
    task = decode(files["task.json"])
    _shape(task, "schema request original request_source inputs context")
    require(task["schema"] == "orchestrator.session-task.v1", "INVALID_SCHEMA", "Task schema")
    request = _validate_request(task["request"])
    attempts = _safe(directory / "attempts")
    require(attempts.is_dir(), "INPUT_UNAVAILABLE", "Task attempts directory missing")
    _shape(task["original"], "path bytes sha256 encoding")
    _shape(task["request_source"], "path bytes sha256")
    for key in ("inputs", "context"):
        rows = _rows(task[key])
        require(len(rows) == len(request[key]), "BINDING_MISMATCH", "Source pin count")
        for row, declared in zip(rows, request[key]):
            _shape(row, "path bytes sha256 id revision")
            require(row["id"] == declared["id"] and row["revision"] == declared["revision"],
                    "BINDING_MISMATCH", "Source pin identity/revision")
    require(directory.name == request["task_id"] and decode(files["request-source.bin"]) == request,
            "BINDING_MISMATCH", "Task/request binding")
    require(sha(files["original.bin"]) == task["original"]["sha256"], "INTEGRITY_MISMATCH", "Original bytes")
    require(sha(files["request-source.bin"]) == task["request_source"]["sha256"],
            "INTEGRITY_MISMATCH", "Request source bytes")
    for pin in [task["original"], task["request_source"], *task["inputs"], *task["context"]]:
        _revalidate(pin)
    return directory, task, digest


def _binding(task, task_hash, attempt_id):
    return {"task_id": task["request"]["task_id"], "attempt_id": attempt_id,
            "task_sha256": task_hash, "original_sha256": task["original"]["sha256"],
            "inputs_sha256": sha(packed(task["inputs"])), "context_sha256": sha(packed(task["context"]))}


def prepare_work(task_dir, attempt_id, *, parent_attempt=None, executor="UNKNOWN"):
    directory, task, task_hash = _task(task_dir)
    _identifier(attempt_id)
    _text(executor)
    if parent_attempt is not None:
        _identifier(parent_attempt)
        require(parent_attempt != attempt_id, "INVALID_PARENT", "Attempt cannot parent itself")
        _attempt(task_dir, parent_attempt)
    attempts = _safe(directory / "attempts")
    require(len(list(attempts.iterdir())) < task["request"]["stop"]["max_attempts"],
            "ATTEMPT_BUDGET", "Explicit attempt cap reached")
    attempt_dir = _mkdir(attempts / attempt_id)
    work_dir = _mkdir(attempt_dir / "work")
    payload = {"schema": "orchestrator.session-work.v1", "binding": _binding(task, task_hash, attempt_id),
               "parent_attempt": parent_attempt, "executor": executor, "work_dir": str(work_dir),
               "request": task["request"], "inputs": task["inputs"], "context": task["context"],
               "original_path": str(directory / "original.bin"), "trust": "LOCAL_DATA_NO_AUTHORITY_OR_DISPATCH"}
    payload["binding"]["packet_sha256"] = sha(packed(payload))
    _commit(attempt_dir, {"packet.json": packed(payload)})
    return {"status": "WORK_PREPARED", **payload}


def _attempt(task_dir, attempt_id):
    directory, task, task_hash = _task(task_dir)
    _identifier(attempt_id)
    attempt_dir = _safe(directory / "attempts" / attempt_id)
    files, _ = _bundle(attempt_dir, {"packet.json"})
    packet = decode(files["packet.json"])
    _shape(packet, "schema binding parent_attempt executor work_dir request inputs context original_path trust")
    expected = _binding(task, task_hash, attempt_id)
    binding = dict(packet["binding"])
    packet_hash = binding.pop("packet_sha256", None)
    payload = {**packet, "binding": binding}
    require(binding == expected and packet_hash == sha(packed(payload)) and packet["request"] == task["request"]
            and packet["inputs"] == task["inputs"] and packet["context"] == task["context"]
            and packet["work_dir"] == str(attempt_dir / "work")
            and packet["original_path"] == str(directory / "original.bin")
            and packet["schema"] == "orchestrator.session-work.v1",
            "BINDING_MISMATCH", "Work packet changed or wrong task/attempt")
    _safe(packet["work_dir"])
    return attempt_dir, task, packet


def _criteria(rows, task, output_ids):
    _unique(_rows(rows))
    allowed = {row["id"] for row in task["request"]["acceptance"]}
    require({row["id"] for row in rows} <= allowed, "INVALID_SCHEMA", "Unknown acceptance ID")
    for row in rows:
        _shape(row, "id status evidence note")
        require(row["status"] in ("SATISFIED", "UNSATISFIED", "BLOCKED"), "INVALID_SCHEMA", "Criterion status")
        _text(row["note"])
        _evidence(row["evidence"], output_ids)
    return rows


def _evidence(refs, output_ids):
    _rows(refs)
    require(all(type(ref) is str and ref in output_ids for ref in refs)
            and len(refs) == len(set(refs)), "INVALID_EVIDENCE", "Evidence must reference captured output IDs")


def _limitations(rows):
    for row in _rows(rows):
        _text(row)


def _outputs(record, task, packet):
    rows = _rows(record["outputs"])
    _unique(rows)
    contract = {row["id"]: row for row in task["request"]["output_contract"]}
    pins = []
    total = 0
    for row in rows:
        _shape(row, "id path")
        require(row["id"] in contract and _relative(row["path"]) == contract[row["id"]]["path"],
                "OUTPUT_BOUNDARY", "Output must match declared ID/path")
        pin = _pin(Path(packet["work_dir"]) / row["path"], id=row["id"], relative_path=row["path"])
        total += pin["bytes"]
        require(total <= task["request"]["stop"]["max_output_bytes"], "BYTE_BUDGET", "Output byte cap")
        pins.append(pin)
    return pins


def _validate_result(record, task, packet):
    _shape(record, "schema binding executor claimed_status outputs criteria limitations")
    require(record["schema"] == "orchestrator.session-result.v1" and record["binding"] == packet["binding"],
            "BINDING_MISMATCH", "Result task/attempt/input/context/packet binding")
    _text(record["executor"])
    require(record["claimed_status"] in ("DONE", "PARTIAL", "BLOCKED"), "INVALID_SCHEMA", "Claimed status")
    pins = _outputs(record, task, packet)
    _criteria(record["criteria"], task, {pin["id"] for pin in pins})
    _limitations(record["limitations"])
    return pins


def record_result(task_dir, attempt_id, result_file):
    attempt_dir, task, packet = _attempt(task_dir, attempt_id)
    raw = _read(result_file, MAX_JSON)
    record = decode(raw)
    pins = _validate_result(record, task, packet)
    receipt = {"schema": "orchestrator.session-result-receipt.v1", "binding": packet["binding"],
               "result_sha256": sha(raw), "outputs": pins, "origin": "UNVERIFIED_CALLER_RECORD",
               "authenticated_acceptance": False}
    _commit(_mkdir(attempt_dir / "result"), {"record.json": raw, "receipt.json": packed(receipt)})
    return {"status": "RESULT_RECORDED", **receipt}


def _result(attempt_dir, task, packet):
    files, _ = _bundle(attempt_dir / "result", {"record.json", "receipt.json"})
    record = decode(files["record.json"])
    pins = _validate_result(record, task, packet)
    expected = {"schema": "orchestrator.session-result-receipt.v1", "binding": packet["binding"],
                "result_sha256": sha(files["record.json"]), "outputs": pins,
                "origin": "UNVERIFIED_CALLER_RECORD", "authenticated_acceptance": False}
    require(decode(files["receipt.json"]) == expected, "STALE_OUTPUT", "Output/result receipt differs")
    return record, expected


def _validate_review(record, task, packet, result_receipt):
    _shape(record, "schema binding result_sha256 reviewer producer provenance evidence criteria limitations")
    require(record["schema"] == "orchestrator.session-review.v1" and record["binding"] == packet["binding"]
            and record["result_sha256"] == result_receipt["result_sha256"],
            "BINDING_MISMATCH", "Review task/attempt/result binding")
    for key in ("reviewer", "producer", "provenance"):
        _text(record[key])
    ids = {pin["id"] for pin in result_receipt["outputs"]}
    _evidence(record["evidence"], ids)
    _criteria(record["criteria"], task, ids)
    _limitations(record["limitations"])


def record_review(task_dir, attempt_id, review_file):
    attempt_dir, task, packet = _attempt(task_dir, attempt_id)
    _, result_receipt = _result(attempt_dir, task, packet)
    raw = _read(review_file, MAX_JSON)
    record = decode(raw)
    _validate_review(record, task, packet, result_receipt)
    receipt = {"schema": "orchestrator.session-review-receipt.v1", "binding": packet["binding"],
               "result_sha256": result_receipt["result_sha256"], "review_sha256": sha(raw),
               "origin": "UNVERIFIED_CALLER_RECORD", "authenticated_acceptance": False}
    _commit(_mkdir(attempt_dir / "review"), {"record.json": raw, "receipt.json": packed(receipt)})
    return {"status": "REVIEW_RECORDED_UNVERIFIED", **receipt}


def _review(attempt_dir, task, packet, result_receipt):
    files, _ = _bundle(attempt_dir / "review", {"record.json", "receipt.json"})
    record = decode(files["record.json"])
    _validate_review(record, task, packet, result_receipt)
    expected = {"schema": "orchestrator.session-review-receipt.v1", "binding": packet["binding"],
                "result_sha256": result_receipt["result_sha256"], "review_sha256": sha(files["record.json"]),
                "origin": "UNVERIFIED_CALLER_RECORD", "authenticated_acceptance": False}
    require(decode(files["receipt.json"]) == expected, "INTEGRITY_MISMATCH", "Review receipt changed")
    return record


def check(task_dir, attempt_id=None):
    """Return mechanical state. Invalid/stale bytes raise SessionError; no semantic verdict."""
    if attempt_id is None:
        directory, task, task_hash = _task(task_dir)
    else:
        attempt_dir, task, packet = _attempt(task_dir, attempt_id)
        directory = attempt_dir.parent.parent
        task_hash = packet["binding"]["task_sha256"]
    # Surface the preserved original beside the caller's derived goal. These
    # declarations are not an independently verified oracle for the original.
    goal_review = {
        "preserved_original": {"path": str(directory / "original.bin"),
                               "source_path": task["original"]["path"],
                               "sha256": task["original"]["sha256"],
                               "bytes": task["original"]["bytes"],
                               "encoding": task["original"]["encoding"]},
        "declared_objective": task["request"]["objective"],
        "declared_scope": task["request"]["scope"],
        "declared_acceptance": task["request"]["acceptance"],
        "acceptance_origin": "CALLER_DECLARED_NOT_VERIFIED_ORIGINAL_ORACLE",
        "decision_provenance": task["request"]["decision_provenance"],
        "alignment": "UNVERIFIED_REQUIRES_ROOT_COMPARISON",
        "original_goal_resolution": "NOT_ESTABLISHED",
    }
    base = {"task_id": task["request"]["task_id"], "task_sha256": task_hash,
            "mechanical_integrity": True, "authenticated_acceptance": False, "full_completion": False,
            "dependencies": task["request"]["dependencies"], "goal_review": goal_review}
    if attempt_id is None:
        attempts = _safe(directory / "attempts")
        return {**base, "status": "TASK_VALID", "attempts": sorted(p.name for p in attempts.iterdir())}
    base.update(attempt_id=attempt_id, binding=packet["binding"], work_dir=packet["work_dir"])
    if not os.path.lexists(attempt_dir / "result"):
        return {**base, "status": "PENDING_RESULT", "mechanical_candidate_ready": False}
    result, receipt = _result(attempt_dir, task, packet)
    output_ids = {pin["id"] for pin in receipt["outputs"]}
    gaps = ["output:" + row["id"] for row in task["request"]["output_contract"] if row["required"] and row["id"] not in output_ids]
    gaps += ["dependency:" + row["id"] for row in task["request"]["dependencies"] if row["required"] and row["status"] == "BLOCKED"]
    if result["claimed_status"] != "DONE":
        gaps.append("result:claimed-" + result["claimed_status"].lower())
    for acceptance in task["request"]["acceptance"]:
        if acceptance["required"]:
            criterion = next((row for row in result["criteria"] if row["id"] == acceptance["id"]), None)
            if criterion is None or criterion["status"] != "SATISFIED" or not criterion["evidence"]:
                gaps.append("result-criterion:" + acceptance["id"])
    review = None
    if os.path.lexists(attempt_dir / "review"):
        review = _review(attempt_dir, task, packet, receipt)
        for acceptance in task["request"]["acceptance"]:
            if acceptance["required"]:
                criterion = next((row for row in review["criteria"] if row["id"] == acceptance["id"]), None)
                if criterion is None or criterion["status"] != "SATISFIED" or not criterion["evidence"]:
                    gaps.append("review-criterion:" + acceptance["id"])
        if not review["evidence"]:
            gaps.append("review:evidence")
    else:
        gaps.append("review:missing")
    return {**base, "status": "REVIEW_RECORDED_UNVERIFIED" if review else "PENDING_REVIEW",
            "outputs": receipt["outputs"], "result_sha256": receipt["result_sha256"], "gaps": gaps,
            "mechanical_candidate_ready": not gaps, "claimed_status": result["claimed_status"],
            "result_criteria": result["criteria"], "review_criteria": review["criteria"] if review else [],
            "review_origin": "UNVERIFIED_CALLER_RECORD" if review else "NONE"}


def report(task_dir, attempt_id=None):
    """Read-only report; file existence and reviewer labels never establish completion."""
    result = check(task_dir, attempt_id)
    return {**result, "scope": "LOCAL_FILE_LIFECYCLE_ONLY", "semantic_acceptance": "PENDING_INDEPENDENT_ROOT_REVIEW",
            "authority": "NOT_IMPLEMENTED", "dispatch": "NOT_IMPLEMENTED",
            "limitations": ["No authentication of producer/reviewer or semantic correctness",
                            "No OS sandbox or hostile concurrent filesystem protection",
                            "Local manifests provide consistency, not adversary-resistant authenticity"]}
