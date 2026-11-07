"""Contract tests for the local, file-only session controller.

Run by the root executor after the frozen test packet is approved. Fixtures are
created beneath the workspace's local-runs directory, never the OS temp folder.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
RUNS_ROOT = WORKSPACE_ROOT / "local-runs"
RUNS_ROOT.mkdir(exist_ok=True)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from orchestrator_session import core  # noqa: E402
from orchestrator_session.core import SessionError  # noqa: E402


class SessionFixture:
    """Build request/result/review documents from the public schema."""

    def __init__(self, root: Path, task_id: str = "task-contract-01"):
        self.root = root
        self.source_dir = root / "sources"
        self.source_dir.mkdir(parents=True)
        self.original_bytes = "Yêu cầu gốc\r\nGiữ nguyên dòng thứ hai\r\n".encode("utf-8")
        self.input_bytes = b"input revision one\r\n"
        self.context_bytes = b"context revision one\r\n"
        (self.source_dir / "original.txt").write_bytes(self.original_bytes)
        (self.source_dir / "input.txt").write_bytes(self.input_bytes)
        (self.source_dir / "context.txt").write_bytes(self.context_bytes)
        self.request = {
            "schema": "orchestrator.session-request.v1",
            "task_id": task_id,
            "original": {"path": "original.txt", "encoding": "utf-8"},
            "objective": "Change the sample output while preserving the requested bytes in the source record.",
            "scope": "A local text artifact only.",
            "decision_provenance": "Explicit local test fixture request.",
            "owner": "Evidence-Synthesizer",
            "acceptance": [{"id": "criterion-1", "description": "The requested output content is present.", "required": True}],
            "inputs": [{"id": "input-1", "path": "input.txt", "revision": "r1"}],
            "context": [{"id": "context-1", "path": "context.txt", "revision": "r1"}],
            "selected_skills": [],
            "rejected_skills": [],
            "dependencies": [],
            "output_contract": [{"id": "output-1", "path": "artifacts/result.txt", "required": True}],
            "stop": {"max_attempts": 3, "max_output_bytes": 16384, "note": "Stop after the bounded local change."},
        }
        self.request_path = self.source_dir / "request.json"
        self.write_json(self.request_path, self.request, crlf=True)
        self.output_root = root / "run-output"
        self.output_root.mkdir()
        self.created = None
        self.task_dir = None
        self.attempt = None
        self.packet = None
        self.result_path = None
        self.result = None
        self.output_path = None

    @staticmethod
    def write_json(path: Path, value, crlf: bool = False):
        text = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)
        if crlf:
            text = text.replace("\n", "\r\n")
        path.write_bytes(text.encode("utf-8"))

    def create(self):
        self.created = core.create(str(self.request_path), str(self.output_root))
        self.task_dir = Path(self.created["task_dir"])
        return self.created

    def prepare(self, attempt_id="attempt-01", parent_attempt=None):
        if self.task_dir is None:
            self.create()
        self.attempt = attempt_id
        self.packet = core.prepare_work(str(self.task_dir), attempt_id, parent_attempt=parent_attempt, executor="UNKNOWN")
        return self.packet

    def make_result(self, *, claimed_status="DONE", output_content=b"verified local output\r\n", criteria=None, binding=None):
        if self.packet is None:
            self.prepare()
        self.output_path = Path(self.packet["work_dir"]) / "artifacts" / "result.txt"
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        if output_content is not None:
            self.output_path.write_bytes(output_content)
        self.result = {
            "schema": "orchestrator.session-result.v1",
            "binding": binding if binding is not None else self.packet["binding"],
            "executor": "UNKNOWN",
            "claimed_status": claimed_status,
            "outputs": [{"id": "output-1", "path": "artifacts/result.txt"}] if output_content is not None else [],
            "criteria": criteria if criteria is not None else [{"id": "criterion-1", "status": "SATISFIED", "evidence": ["output-1"], "note": "Fixture claim; semantic validity is not asserted."}],
            "limitations": ["Fixture does not prove semantic correctness."],
        }
        self.result_path = self.root / f"{self.attempt}-result.json"
        self.write_json(self.result_path, self.result)
        return self.result_path

    def record_result(self, **kwargs):
        if self.packet is None:
            self.prepare()
        result_path = self.make_result(**kwargs)
        return core.record_result(str(self.task_dir), self.attempt, str(result_path))

    def make_review(self, result_receipt, *, reviewer="Orchestrator", provenance="session label; unauthenticated", criteria=None, evidence=None, result_sha256=None, binding=None):
        review = {
            "schema": "orchestrator.session-review.v1",
            "binding": binding if binding is not None else self.packet["binding"],
            "result_sha256": result_sha256 if result_sha256 is not None else result_receipt["result_sha256"],
            "reviewer": reviewer,
            "producer": "test-fixture",
            "provenance": provenance,
            "evidence": evidence if evidence is not None else ["output-1"],
            "criteria": criteria if criteria is not None else [{"id": "criterion-1", "status": "SATISFIED", "evidence": ["output-1"], "note": "Fixture review claim; not authenticated."}],
            "limitations": ["Fixture review is unverified."],
        }
        review_path = self.root / f"{self.attempt}-review.json"
        self.write_json(review_path, review)
        return review_path

    def record_review(self, result_receipt, **kwargs):
        review_path = self.make_review(result_receipt, **kwargs)
        return core.record_review(str(self.task_dir), self.attempt, str(review_path))


class SessionControllerContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="session-controller-test-", dir=RUNS_ROOT)
        self.root = Path(self.temp.name).resolve()
        if self.root.parent != RUNS_ROOT.resolve():
            self.temp.cleanup()
            self.fail("Fixture directory escaped the designated workspace local-runs root.")
        self.addCleanup(self._safe_cleanup)
        self.fx = SessionFixture(self.root)

    def _safe_cleanup(self):
        resolved = Path(self.temp.name).resolve()
        if resolved.parent != RUNS_ROOT.resolve():
            raise RuntimeError("Refusing to clean a fixture outside the designated workspace local-runs root")
        self.temp.cleanup()

    def test_original_unicode_crlf_bytes_are_preserved(self):
        created = self.fx.create()
        task_dir = Path(created["task_dir"])
        self.assertEqual((task_dir / "original.bin").read_bytes(), self.fx.original_bytes)
        task = json.loads((task_dir / "task.json").read_text(encoding="utf-8"))
        self.assertEqual(task["original"]["bytes"], len(self.fx.original_bytes))
        self.assertEqual(task["original"]["sha256"], hashlib.sha256(self.fx.original_bytes).hexdigest())
        self.assertEqual(task["request"]["objective"], self.fx.request["objective"])
        self.assertTrue(self.fx.request_path.read_bytes().count(b"\r\n") > 0)
        self.assertEqual((task_dir / "request-source.bin").read_bytes(), self.fx.request_path.read_bytes())

    def test_changed_original_input_context_and_output_are_detected(self):
        for source_name in ("original.txt", "input.txt", "context.txt"):
            with self.subTest(source=source_name):
                fx = SessionFixture(self.root / source_name.replace(".", "-"))
                fx.create()
                fx.prepare()
                source = fx.source_dir / source_name
                source.write_bytes(source.read_bytes() + b"changed")
                with self.assertRaises(SessionError) as raised:
                    core.check(str(fx.task_dir), fx.attempt)
                self.assertEqual(raised.exception.code, "STALE_SOURCE")

        fx = SessionFixture(self.root / "output-stale")
        fx.create()
        fx.prepare()
        fx.record_result()
        fx.output_path.write_bytes(b"changed after receipt")
        with self.assertRaises(SessionError) as raised:
            core.check(str(fx.task_dir), fx.attempt)
        self.assertEqual(raised.exception.code, "STALE_OUTPUT")

    def test_result_and_review_wrong_task_attempt_or_digest_are_rejected(self):
        for binding_change in (
            {"task_id": "other-task"},
            {"attempt_id": "other-attempt"},
            {"inputs_sha256": "0" * 64},
            {"context_sha256": "0" * 64},
            {"task_sha256": "0" * 64},
        ):
            with self.subTest(binding=binding_change):
                fx = SessionFixture(self.root / ("result-" + next(iter(binding_change))))
                fx.create()
                packet = fx.prepare()
                binding = dict(packet["binding"])
                binding.update(binding_change)
                result_path = fx.make_result(binding=binding)
                with self.assertRaises(SessionError) as raised:
                    core.record_result(str(fx.task_dir), fx.attempt, str(result_path))
                self.assertEqual(raised.exception.code, "BINDING_MISMATCH")

        for change in ("task_id", "attempt_id", "inputs_sha256", "context_sha256"):
            with self.subTest(review_binding=change):
                fx = SessionFixture(self.root / ("review-" + change))
                fx.create()
                packet = fx.prepare()
                result_receipt = fx.record_result()
                binding = dict(packet["binding"])
                binding[change] = "wrong-binding"
                review_path = fx.make_review(result_receipt, binding=binding)
                with self.assertRaises(SessionError) as raised:
                    core.record_review(str(fx.task_dir), fx.attempt, str(review_path))
                self.assertEqual(raised.exception.code, "BINDING_MISMATCH")

        fx = SessionFixture(self.root / "review-result-digest")
        fx.create()
        fx.prepare()
        result_receipt = fx.record_result()
        review_path = fx.make_review(result_receipt, result_sha256="0" * 64)
        with self.assertRaises(SessionError) as raised:
            core.record_review(str(fx.task_dir), fx.attempt, str(review_path))
        self.assertEqual(raised.exception.code, "BINDING_MISMATCH")

    def test_review_pass_claim_does_not_authenticate_semantic_completion(self):
        self.fx.create()
        self.fx.prepare()
        result_receipt = self.fx.record_result()
        self.fx.record_review(result_receipt, reviewer="Orchestrator", provenance="PASS")
        state = core.check(str(self.fx.task_dir), self.fx.attempt)
        report = core.report(str(self.fx.task_dir), self.fx.attempt)
        self.assertTrue(state["mechanical_integrity"])
        self.assertTrue(state["mechanical_candidate_ready"])
        self.assertFalse(state["authenticated_acceptance"])
        self.assertFalse(state["full_completion"])
        self.assertEqual(state["review_origin"], "UNVERIFIED_CALLER_RECORD")
        self.assertFalse(report["authenticated_acceptance"])
        self.assertFalse(report["full_completion"])
        self.assertEqual(report["semantic_acceptance"], "PENDING_INDEPENDENT_ROOT_REVIEW")

    def test_missing_required_criteria_evidence_or_output_prevents_completion(self):
        self.fx.create()
        self.fx.prepare()
        self.fx.record_result(output_content=None, criteria=[])
        state = core.check(str(self.fx.task_dir), self.fx.attempt)
        self.assertFalse(state["mechanical_candidate_ready"])
        self.assertIn("output:output-1", state["gaps"])
        self.assertIn("result-criterion:criterion-1", state["gaps"])
        self.assertIn("review:missing", state["gaps"])
        self.assertFalse(core.report(str(self.fx.task_dir), self.fx.attempt)["full_completion"])

        fx = SessionFixture(self.root / "empty-evidence")
        fx.create()
        fx.prepare()
        result_receipt = fx.record_result(criteria=[{"id": "criterion-1", "status": "SATISFIED", "evidence": [], "note": "No evidence."}])
        fx.record_review(result_receipt, evidence=[], criteria=[{"id": "criterion-1", "status": "SATISFIED", "evidence": [], "note": "No evidence."}])
        state = core.check(str(fx.task_dir), fx.attempt)
        self.assertFalse(state["mechanical_candidate_ready"])
        self.assertIn("result-criterion:criterion-1", state["gaps"])
        self.assertIn("review-criterion:criterion-1", state["gaps"])
        self.assertIn("review:evidence", state["gaps"])

    def test_retry_creates_immutable_attempt_history(self):
        self.fx.create()
        first = self.fx.prepare("attempt-01")
        first_result = self.fx.record_result()
        first_attempt_dir = Path(first["work_dir"]).parent
        packet_bytes = (first_attempt_dir / "packet.json").read_bytes()
        result_record_bytes = (first_attempt_dir / "result" / "record.json").read_bytes()

        second = core.prepare_work(str(self.fx.task_dir), "attempt-02", parent_attempt="attempt-01")
        self.assertEqual(second["binding"]["attempt_id"], "attempt-02")
        self.assertEqual((first_attempt_dir / "packet.json").read_bytes(), packet_bytes)
        self.assertEqual((first_attempt_dir / "result" / "record.json").read_bytes(), result_record_bytes)
        self.assertEqual(core.check(str(self.fx.task_dir), "attempt-01")["result_sha256"], first_result["result_sha256"])
        with self.assertRaises(SessionError) as raised:
            core.prepare_work(str(self.fx.task_dir), "attempt-01")
        self.assertEqual(raised.exception.code, "OUTPUT_EXISTS")

    def test_review_retry_rejects_overwrite_and_preserves_original_raw_fields(self):
        self.fx.create()
        self.fx.prepare()
        result_receipt = self.fx.record_result()
        first_path = self.fx.make_review(result_receipt, reviewer="reviewer-first", provenance="original review provenance")
        core.record_review(str(self.fx.task_dir), self.fx.attempt, str(first_path))
        review_dir = Path(self.fx.task_dir) / "attempts" / self.fx.attempt / "review"
        record_path = review_dir / "record.json"
        receipt_path = review_dir / "receipt.json"
        original_record = record_path.read_bytes()
        original_receipt = receipt_path.read_bytes()

        replacement_path = self.fx.make_review(result_receipt, reviewer="reviewer-second", provenance="replacement attempt")
        with self.assertRaises(SessionError) as raised:
            core.record_review(str(self.fx.task_dir), self.fx.attempt, str(replacement_path))
        self.assertEqual(raised.exception.code, "OUTPUT_EXISTS")
        self.assertEqual(record_path.read_bytes(), original_record)
        self.assertEqual(receipt_path.read_bytes(), original_receipt)
        preserved = json.loads(record_path.read_text(encoding="utf-8"))
        self.assertEqual(preserved["reviewer"], "reviewer-first")
        self.assertEqual(preserved["provenance"], "original review provenance")

    def test_windows_extended_namespace_alias_to_public_output_is_rejected_before_write(self):
        if os.name != "nt":
            self.skipTest("Windows extended namespace aliases are specific to Windows.")
        fx = SessionFixture(self.root / "extended-alias")
        target = REPO_ROOT / "local-runs" / ("forbidden-" + self.root.name)
        self.assertFalse(os.path.lexists(target))
        extended_target = "\\\\?\\" + str(target)
        with self.assertRaises(SessionError) as raised:
            core.create(str(fx.request_path), extended_target)
        self.assertEqual(raised.exception.code, "OUTPUT_BOUNDARY")
        self.assertFalse(os.path.lexists(target), "Boundary validation must happen before any output write.")

    def test_attempts_directory_symlink_is_rejected_by_task_level_check(self):
        self.fx.create()
        task_attempts = Path(self.fx.task_dir) / "attempts"
        redirected_attempts = self.root / "attempts-target"
        redirected_attempts.mkdir()
        task_attempts.rmdir()
        try:
            task_attempts.symlink_to(redirected_attempts, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Host does not permit creating an attempts-directory symlink: {exc}")
        with self.assertRaises(SessionError) as raised:
            core.check(str(self.fx.task_dir))
        self.assertEqual(raised.exception.code, "UNSAFE_PATH")

    def test_path_traversal_and_public_repo_output_root_are_rejected(self):
        fx = SessionFixture(self.root / "traversal")
        fx.request["output_contract"][0]["path"] = "../escape.txt"
        fx.write_json(fx.request_path, fx.request)
        with self.assertRaises(SessionError) as raised:
            core.create(str(fx.request_path), str(fx.output_root))
        self.assertEqual(raised.exception.code, "UNSAFE_PATH")

        fx = SessionFixture(self.root / "public-boundary")
        with self.assertRaises(SessionError) as raised:
            core.create(str(fx.request_path), str(REPO_ROOT / "local-runs" / "forbidden"))
        self.assertEqual(raised.exception.code, "OUTPUT_BOUNDARY")

        fx = SessionFixture(self.root / "result-traversal")
        fx.create()
        fx.prepare()
        result_path = fx.make_result()
        result = dict(fx.result)
        result["outputs"] = [{"id": "output-1", "path": "../escape.txt"}]
        fx.write_json(result_path, result)
        with self.assertRaises(SessionError) as raised:
            core.record_result(str(fx.task_dir), fx.attempt, str(result_path))
        self.assertEqual(raised.exception.code, "UNSAFE_PATH")

    def test_blocked_dependency_preserves_independent_ready_branch(self):
        self.fx.request["dependencies"] = [
            {"id": "blocked-branch", "status": "BLOCKED", "reason": "Required external tool unavailable.", "required": True},
            {"id": "ready-branch", "status": "READY", "reason": "Local file branch is available.", "required": False},
        ]
        self.fx.write_json(self.fx.request_path, self.fx.request)
        self.fx.create()
        self.fx.prepare()
        self.fx.record_result()
        state = core.report(str(self.fx.task_dir), self.fx.attempt)
        self.assertIn("output-1", {output["id"] for output in state["outputs"]})
        self.assertIn("dependency:blocked-branch", state["gaps"])
        self.assertFalse(state["full_completion"])

    def test_partial_write_failure_does_not_leave_success_receipt(self):
        self.fx.create()
        original_atomic = core._atomic

        def fail_manifest(path, raw):
            if Path(path).name == "manifest.json":
                raise SessionError("IO_ERROR", "simulated interruption before manifest publication")
            return original_atomic(path, raw)

        with mock.patch.object(core, "_atomic", side_effect=fail_manifest):
            with self.assertRaises(SessionError) as raised:
                core.prepare_work(str(self.fx.task_dir), "attempt-partial")
        self.assertEqual(raised.exception.code, "IO_ERROR")
        attempt_dir = Path(self.fx.task_dir) / "attempts" / "attempt-partial"
        self.assertTrue((attempt_dir / "packet.json").exists())
        self.assertFalse((attempt_dir / "manifest.json").exists())
        self.assertFalse((attempt_dir / "result" / "receipt.json").exists())
        with self.assertRaises(SessionError):
            core.check(str(self.fx.task_dir), "attempt-partial")

    def test_symlink_output_escape_is_rejected_or_explicitly_skipped(self):
        self.fx.create()
        packet = self.fx.prepare()
        work = Path(packet["work_dir"])
        (work / "artifacts").mkdir()
        outside = self.root / "outside-secret.txt"
        outside.write_bytes(b"outside")
        target = work / "artifacts" / "result.txt"
        try:
            target.symlink_to(outside)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Host does not permit creating a symlink fixture: {exc}")
        result_path = self.fx.make_result(output_content=None)
        result = dict(self.fx.result)
        result["outputs"] = [{"id": "output-1", "path": "artifacts/result.txt"}]
        self.fx.write_json(result_path, result)
        with self.assertRaises(SessionError) as raised:
            core.record_result(str(self.fx.task_dir), self.fx.attempt, str(result_path))
        self.assertEqual(raised.exception.code, "UNSAFE_PATH")

    def test_cli_completes_actual_local_create_prepare_record_check_report_flow(self):
        fx = SessionFixture(self.root / "cli")

        def run(*args):
            command = [sys.executable, str(REPO_ROOT / "scripts" / "session_task.py"), *map(str, args)]
            return subprocess.run(command, cwd=REPO_ROOT, capture_output=True, check=False)

        created = run("create", "--request", fx.request_path, "--output-root", fx.output_root)
        self.assertEqual(created.returncode, 0, created.stderr.decode("utf-8", errors="replace"))
        task_dir = Path(json.loads(created.stdout.decode("utf-8"))["task_dir"])
        prepared = run("prepare-work", "--task-dir", task_dir, "--attempt-id", "cli-attempt")
        self.assertEqual(prepared.returncode, 0, prepared.stderr.decode("utf-8", errors="replace"))
        packet = json.loads(prepared.stdout.decode("utf-8"))
        output = Path(packet["work_dir"]) / "artifacts" / "result.txt"
        output.parent.mkdir(parents=True)
        output.write_bytes(b"CLI output\r\n")
        result = {
            "schema": "orchestrator.session-result.v1", "binding": packet["binding"],
            "executor": "UNKNOWN", "claimed_status": "DONE",
            "outputs": [{"id": "output-1", "path": "artifacts/result.txt"}],
            "criteria": [{"id": "criterion-1", "status": "SATISFIED", "evidence": ["output-1"], "note": "CLI fixture."}],
            "limitations": ["CLI integration fixture."],
        }
        result_path = fx.root / "cli-result.json"
        fx.write_json(result_path, result)
        recorded = run("record-result", "--task-dir", task_dir, "--attempt-id", "cli-attempt", "--result", result_path)
        self.assertEqual(recorded.returncode, 0, recorded.stderr.decode("utf-8", errors="replace"))
        check = run("check", "--task-dir", task_dir, "--attempt-id", "cli-attempt")
        self.assertEqual(check.returncode, 0, check.stderr.decode("utf-8", errors="replace"))
        check_data = json.loads(check.stdout.decode("utf-8"))
        self.assertTrue(check_data["mechanical_integrity"])
        self.assertFalse(check_data["authenticated_acceptance"])
        report = run("report", "--task-dir", task_dir, "--attempt-id", "cli-attempt")
        report_data = json.loads(report.stdout.decode("utf-8"))
        self.assertEqual(report.returncode, 0, report_data)
        self.assertFalse(report_data["full_completion"])
        self.assertEqual(report_data["semantic_acceptance"], "PENDING_INDEPENDENT_ROOT_REVIEW")


if __name__ == "__main__":
    unittest.main()
