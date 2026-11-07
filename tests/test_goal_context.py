"""Visibility checks for original and caller-declared goals; no semantic oracle.

Only synthetic local text artifacts are used. No providers or targets run.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNS_ROOT = REPO_ROOT.parent / "local-runs"
TESTS_ROOT = REPO_ROOT / "tests"
for path in (REPO_ROOT, TESTS_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from orchestrator_session import core  # noqa: E402
from test_session_controller import SessionFixture  # noqa: E402


class GoalContextTests(unittest.TestCase):
    def setUp(self):
        RUNS_ROOT.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="goal-context-test-", dir=RUNS_ROOT)
        self.root = Path(self.temp.name).resolve()
        if self.root.parent != RUNS_ROOT.resolve():
            raise RuntimeError("Fixture escaped the designated local-runs root")
        self.addCleanup(self._safe_cleanup)
        self.fx = SessionFixture(self.root)
        self.original = "Explain every processing stage of the sample format.\r\n"
        self.fx.original_bytes = self.original.encode("utf-8")
        (self.fx.source_dir / "original.txt").write_bytes(self.fx.original_bytes)
        self.fx.request["objective"] = "Chẩn đoán một header lỗi trong mẫu định dạng."
        self.fx.request["scope"] = "Chỉ header lỗi; chưa xét toàn bộ luồng xử lý."
        self.fx.request["acceptance"][0]["description"] = "Mô tả lỗi của header."
        self.fx.request["decision_provenance"] = "DECLINED original; user approved replacement"
        self.fx.write_json(self.fx.request_path, self.fx.request)

    def _safe_cleanup(self):
        if Path(self.temp.name).resolve().parent != RUNS_ROOT.resolve():
            raise RuntimeError("Refusing to clean outside the designated local-runs root")
        self.temp.cleanup()

    def assert_goal_visible(self, state):
        goal = state["goal_review"]
        self.assertEqual(goal["preserved_original"]["path"], str(self.fx.task_dir / "original.bin"))
        self.assertEqual(goal["preserved_original"]["source_path"], str(self.fx.source_dir / "original.txt"))
        self.assertEqual(goal["preserved_original"]["sha256"], hashlib.sha256(self.fx.original_bytes).hexdigest())
        self.assertEqual(goal["preserved_original"]["bytes"], len(self.fx.original_bytes))
        self.assertEqual(goal["preserved_original"]["encoding"], "utf-8")
        self.assertEqual(goal["declared_objective"], self.fx.request["objective"])
        self.assertEqual(goal["declared_scope"], self.fx.request["scope"])
        self.assertEqual(goal["declared_acceptance"], self.fx.request["acceptance"])
        self.assertEqual(goal["acceptance_origin"], "CALLER_DECLARED_NOT_VERIFIED_ORIGINAL_ORACLE")
        self.assertEqual(goal["decision_provenance"], self.fx.request["decision_provenance"])
        self.assertEqual(goal["alignment"], "UNVERIFIED_REQUIRES_ROOT_COMPARISON")
        self.assertEqual(goal["original_goal_resolution"], "NOT_ESTABLISHED")
        self.assertFalse(state["full_completion"])
        # The report exposes the original's reference, not its raw contents.
        self.assertNotIn(self.original.strip(), json.dumps(state, ensure_ascii=False))

    def test_task_and_pending_attempt_reports_expose_goal_context(self):
        self.fx.create()
        task_state = core.report(self.fx.task_dir)
        self.assertEqual(task_state["status"], "TASK_VALID")
        self.assert_goal_visible(task_state)
        self.fx.prepare()
        pending = core.report(self.fx.task_dir, self.fx.attempt)
        self.assertEqual(pending["status"], "PENDING_RESULT")
        self.assert_goal_visible(pending)
        self.fx.record_result()
        pending_review = core.report(self.fx.task_dir, self.fx.attempt)
        self.assertEqual(pending_review["status"], "PENDING_REVIEW")
        self.assert_goal_visible(pending_review)

    def test_done_reviewed_alternative_never_establishes_original_alignment(self):
        receipt = self.fx.record_result()
        self.fx.record_review(receipt)
        with mock.patch.object(core, "_task", wraps=core._task) as task_reader:
            state = core.report(self.fx.task_dir, self.fx.attempt)
        self.assertEqual(task_reader.call_count, 1)
        self.assertEqual(state["claimed_status"], "DONE")
        self.assertTrue(state["mechanical_candidate_ready"])
        self.assertFalse(state["authenticated_acceptance"])
        self.assertEqual(state["semantic_acceptance"], "PENDING_INDEPENDENT_ROOT_REVIEW")
        # A caller's prose claim is surfaced, never treated as a user decision.
        self.assertEqual(state["goal_review"]["decision_provenance"],
                         "DECLINED original; user approved replacement")
        self.assert_goal_visible(state)

    def test_stale_original_fails_instead_of_emitting_goal_context(self):
        self.fx.prepare()
        (self.fx.source_dir / "original.txt").write_bytes(b"changed source\n")
        for attempt_id in (None, self.fx.attempt):
            with self.subTest(attempt_id=attempt_id):
                with self.assertRaises(core.SessionError) as raised:
                    core.report(self.fx.task_dir, attempt_id)
                self.assertEqual(raised.exception.code, "STALE_SOURCE")

    def test_direct_cli_report_includes_goal_context(self):
        receipt = self.fx.record_result()
        self.fx.record_review(receipt)
        completed = subprocess.run(
            [sys.executable, "-I", "-B", str(REPO_ROOT / "scripts" / "session_task.py"),
             "report", "--task-dir", str(self.fx.task_dir), "--attempt-id", self.fx.attempt],
            cwd=REPO_ROOT, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr.decode("utf-8", errors="replace"))
        self.assert_goal_visible(json.loads(completed.stdout.decode("utf-8")))


if __name__ == "__main__":
    unittest.main()
