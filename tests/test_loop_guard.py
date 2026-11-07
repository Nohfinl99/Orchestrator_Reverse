"""Bounded contract tests for the opt-in local loop guard.

These tests use the existing v1 SessionFixture and synthetic local evidence.
They do not dispatch workers, tools, providers, or targets.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
RUNS_ROOT = WORKSPACE_ROOT / "local-runs"
TESTS_ROOT = REPO_ROOT / "tests"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(TESTS_ROOT) not in sys.path:
    sys.path.insert(0, str(TESTS_ROOT))

from orchestrator_session import loop_guard, trace_review  # noqa: E402
from orchestrator_session.core import SessionError  # noqa: E402
from test_session_controller import SessionFixture  # noqa: E402


class LoopGuardContractTests(unittest.TestCase):
    def setUp(self):
        RUNS_ROOT.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="loop-guard-test-", dir=RUNS_ROOT)
        self.root = Path(self.temp.name).resolve()
        if self.root.parent != RUNS_ROOT.resolve():
            self.temp.cleanup()
            self.fail("Fixture directory escaped the designated workspace local-runs root.")
        self.addCleanup(self._safe_cleanup)
        self.fx = self._new_fixture(self.root / "task-one")
        self.ledger = self.root / "ledger"
        self.policy_path = self.root / "policy.json"
        self._write_json(self.policy_path, self._policy())
        self.head = loop_guard.init(str(self.ledger), str(self.policy_path))["head"]

    def _safe_cleanup(self):
        resolved = Path(self.temp.name).resolve()
        if resolved.parent != RUNS_ROOT.resolve():
            raise RuntimeError("Refusing to clean a fixture outside the designated workspace local-runs root")
        self.temp.cleanup()

    @staticmethod
    def _policy(max_attempts=5, *, lineage="lineage-contract", history_complete=True):
        return {
            "schema": "orchestrator.loop-policy.v1",
            "lineage_id": lineage,
            "goal": "Complete the bounded local artifact objective.",
            "caller": "local-root",
            "max_attempts": max_attempts,
            "history_complete": history_complete,
            "history_note": "Synthetic contract fixture history declaration.",
        }

    @staticmethod
    def _write_json(path, value):
        SessionFixture.write_json(Path(path), value)

    @staticmethod
    def _new_fixture(root, task_id="task-contract-01"):
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        fixture = SessionFixture(root, task_id=task_id)
        fixture.request["acceptance"].append({
            "id": "criterion-2", "description": "The independent branch criterion is recorded.", "required": False,
        })
        fixture.write_json(fixture.request_path, fixture.request, crlf=True)
        fixture.create()
        return fixture

    @staticmethod
    def _ref(path):
        path = Path(path)
        raw = path.read_bytes()
        return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}

    def _evidence(self, name="evidence.txt", content=b"criterion-relevant evidence\n"):
        path = self.root / name
        path.write_bytes(content)
        return self._ref(path)

    def _candidate(self, *, fixture=None, attempt="attempt-01", previous=None,
                   operation="read", resource="artifact-A", failure_family="E_IO",
                   criterion="criterion-1", lineage="lineage-contract",
                   goal_revision="goal-r1", progress=None,
                   prerequisites=None):
        fixture = fixture or self.fx
        record = {
            "schema": "orchestrator.loop-candidate.v1",
            "lineage_id": lineage,
            "goal_revision": goal_revision,
            "task_dir": str(fixture.task_dir),
            "attempt_id": attempt,
            "operation": operation,
            "caller": "local-root",
            "criterion_id": criterion,
            "resource": resource,
            "failure_family": failure_family,
            "previous_observation": previous,
            "prerequisites": [] if prerequisites is None else prerequisites,
            "progress": progress,
        }
        path = self.root / f"candidate-{fixture.request['task_id']}-{attempt}.json"
        self._write_json(path, record)
        return path, record

    def _observation(self, *, fixture=None, attempt="attempt-01", raw=b"read failed\n",
                     operation="read", resource="artifact-A", failure_family="E_IO",
                     goal_revision="goal-r1", noise=None):
        fixture = fixture or self.fx
        if fixture.packet is None or fixture.attempt != attempt:
            fixture.prepare(attempt)
        raw_path = self.root / f"failure-{fixture.request['task_id']}-{attempt}.bin"
        raw_path.write_bytes(raw)
        record = {
            "schema": "orchestrator.loop-observation.v1",
            "lineage_id": "lineage-contract",
            "goal_revision": goal_revision,
            "task_dir": str(fixture.task_dir),
            "attempt_id": attempt,
            "operation": operation,
            "caller": "local-root",
            "criterion_id": "criterion-1",
            "resource": resource,
            "failure_family": failure_family,
            "raw_failure": self._ref(raw_path),
            "noise": [] if noise is None else noise,
            "prerequisites": [],
            "steps": [],
        }
        path = self.root / f"observation-{fixture.request['task_id']}-{attempt}.json"
        self._write_json(path, record)
        return path, record, raw_path

    def _record_observation(self, **kwargs):
        path, record, raw_path = self._observation(**kwargs)
        result = loop_guard.observe(str(self.ledger), self.head, str(path))
        self.head = result["head"]
        return result, record, raw_path

    def test_same_lineage_retry_without_progress_stops(self):
        self.fx.prepare("attempt-01")
        first, _, _ = self._record_observation(attempt="attempt-01")
        candidate, _ = self._candidate(attempt="attempt-02", previous=first["head"])
        report = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(report["status"], "STOP_NO_PROGRESS")
        self.assertEqual(report["used_attempts"], 1)
        self.assertFalse(report["authority_granted"])
        self.assertFalse(report["dispatch"])

    def test_lineage_budget_spans_task_ids_and_goal_revisions(self):
        self.ledger = self.root / "budget-ledger"
        self.policy_path = self.root / "budget-policy.json"
        self._write_json(self.policy_path, self._policy(max_attempts=2))
        self.head = loop_guard.init(str(self.ledger), str(self.policy_path))["head"]
        first_fixture = self.fx
        first_fixture.prepare("task-one-attempt")
        first, _, _ = self._record_observation(fixture=first_fixture, attempt="task-one-attempt")

        second_fixture = self._new_fixture(self.root / "task-two", task_id="task-contract-02")
        second_fixture.prepare("task-two-attempt")
        second, _, _ = self._record_observation(
            fixture=second_fixture, attempt="task-two-attempt", goal_revision="goal-r2")
        self.assertTrue(first["imported"])
        self.assertTrue(second["imported"])
        candidate, _ = self._candidate(
            fixture=second_fixture, attempt="task-two-retry", previous=second["head"],
            goal_revision="goal-r2")
        report = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(report["status"], "STOP_BUDGET")
        self.assertEqual(report["used_attempts"], 2)

    def test_untrusted_progress_waits_until_explicit_bound_root_review(self):
        self.fx.prepare("attempt-01")
        observed, _, _ = self._record_observation(attempt="attempt-01")
        evidence = self._evidence()
        progress = {"kind": "HYPOTHESIS_REFUTED", "note": "Evidence addresses the unmet criterion.",
                    "evidence": [evidence]}
        candidate, _ = self._candidate(attempt="attempt-02", previous=observed["head"], progress=progress)
        pending = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(pending["status"], "WAIT_PROGRESS_REVIEW")
        self.assertFalse(pending["authenticated_review"])
        review = {
            "schema": "orchestrator.loop-review.v1",
            "lineage_id": "lineage-contract",
            "prior_head": self.head,
            "candidate_sha256": pending["candidate_sha256"],
            "previous_observation": observed["head"],
            "reviewer": "root-reviewer",
            "producer": "local-producer",
            "provenance": "root independently inspected the pinned evidence",
            "verdict": "RELEVANT_PROGRESS",
            "evidence": [evidence],
            "rationale": "The evidence bears on the criterion and supports a bounded next attempt.",
        }
        review_path = self.root / "review.json"
        self._write_json(review_path, review)
        reviewed = loop_guard.review(str(self.ledger), self.head, str(review_path))
        self.head = reviewed["head"]
        unselected = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(unselected["status"], "WAIT_PROGRESS_REVIEW")
        accepted = loop_guard.check(str(self.ledger), self.head, str(candidate), root_review=self.head)
        self.assertEqual(accepted["status"], "BOUNDED_RETRY_CANDIDATE")
        self.assertFalse(accepted["authority_granted"])
        self.assertFalse(accepted["authenticated_review"])
        self.assertFalse(accepted["dispatch"])

    def test_stale_current_task_source_blocks_candidate(self):
        candidate, _ = self._candidate()
        input_source = self.fx.source_dir / "input.txt"
        input_source.write_bytes(input_source.read_bytes() + b"stale")
        with self.assertRaises(SessionError) as raised:
            loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(raised.exception.code, "STALE_SOURCE")

    def test_unobserved_reservation_waits_for_evidence(self):
        first, _ = self._candidate(attempt="attempt-01")
        prepared = loop_guard.prepare(str(self.ledger), self.head, str(first))
        self.head = prepared["head"]
        self.assertEqual(prepared["status"], "WORK_PREPARED_GUARDED")
        second, _ = self._candidate(attempt="attempt-02")
        report = loop_guard.check(str(self.ledger), self.head, str(second))
        self.assertEqual(report["status"], "WAIT_EVIDENCE")
        self.assertIn("unobserved_reserved_attempt", report["gaps"])

    def test_same_message_different_branch_context_waits_for_review(self):
        self.fx.prepare("attempt-01")
        first, _, _ = self._record_observation(
            attempt="attempt-01", raw=b"permission denied\n", operation="read", resource="file-A")
        variants = [
            {"operation": "write", "resource": "file-A", "criterion": "criterion-1"},
            {"operation": "read", "resource": "file-B", "criterion": "criterion-1"},
            {"operation": "read", "resource": "file-A", "criterion": "criterion-2"},
        ]
        for index, variant in enumerate(variants, 2):
            with self.subTest(context=variant):
                candidate, _ = self._candidate(
                    attempt=f"attempt-{index:02d}", previous=None, **variant)
                report = loop_guard.check(str(self.ledger), self.head, str(candidate))
                self.assertEqual(report["status"], "WAIT_PROGRESS_REVIEW")
                self.assertEqual(report["used_attempts"], 1)
        self.assertEqual(first["failure_key"]["operation"], "read")
        self.assertEqual(first["failure_key"]["resource"], "file-A")

    def test_uuid_and_timestamp_noise_normalize_without_losing_raw_failures(self):
        identifiers = ["a5e1d19f-47d6-4b58-8f92-43e265bd3b08",
                      "c176a4b0-d97d-42dd-9d02-1aa50d225bb9"]
        timestamps = ["2026-10-31T10:11:12Z", "2026-11-01T12:13:14Z"]
        outputs = []
        for index, (identifier, timestamp) in enumerate(zip(identifiers, timestamps), 1):
            attempt = f"attempt-{index:02d}"
            self.fx.prepare(attempt)
            noise = [{"kind": "UUID", "value": identifier},
                     {"kind": "TIMESTAMP", "value": timestamp}]
            result, _, raw_path = self._record_observation(
                attempt=attempt, raw=f"request {identifier} failed at {timestamp}\n".encode(), noise=noise)
            outputs.append((result, raw_path.read_bytes()))
        self.assertEqual(outputs[0][0]["normalization"]["sha256"],
                         outputs[1][0]["normalization"]["sha256"])
        self.assertNotEqual(outputs[0][0]["normalization"]["raw_sha256"],
                            outputs[1][0]["normalization"]["raw_sha256"])
        self.assertNotEqual(outputs[0][1], outputs[1][1])

    def test_nontext_failure_keeps_signature_unknown_and_waits_for_review(self):
        self.fx.prepare("attempt-01")
        observed, _, raw_path = self._record_observation(attempt="attempt-01", raw=b"\xff\xfe\x00")
        self.assertEqual(raw_path.read_bytes(), b"\xff\xfe\x00")
        candidate, _ = self._candidate(attempt="attempt-02", previous=observed["head"])
        report = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(report["status"], "WAIT_PROGRESS_REVIEW")

    def test_tampered_truncated_and_gapped_ledgers_fail_closed(self):
        for defect in ("tampered", "truncated", "gap"):
            with self.subTest(defect=defect):
                ledger = self.root / f"ledger-{defect}"
                policy_path = self.root / f"policy-{defect}.json"
                self._write_json(policy_path, self._policy())
                head = loop_guard.init(str(ledger), str(policy_path))["head"]
                first_event = ledger / "00000001"
                if defect == "tampered":
                    event_path = first_event / "event.json"
                    raw = event_path.read_bytes()
                    event_path.write_bytes(raw + b" ")
                elif defect == "truncated":
                    import shutil
                    shutil.rmtree(first_event)
                else:
                    (ledger / "00000003").mkdir()
                with self.assertRaises(SessionError):
                    loop_guard.check(str(ledger), head, str(self._candidate()[0]))

    def test_incomplete_history_waits_and_malformed_lineage_is_rejected(self):
        incomplete_ledger = self.root / "incomplete-ledger"
        incomplete_policy = self.root / "incomplete-policy.json"
        self._write_json(incomplete_policy, self._policy(history_complete=False))
        head = loop_guard.init(str(incomplete_ledger), str(incomplete_policy))["head"]
        candidate, _ = self._candidate()
        report = loop_guard.check(str(incomplete_ledger), head, str(candidate))
        self.assertEqual(report["status"], "WAIT_EVIDENCE")
        self.assertIn("history_incomplete", report["gaps"])

        malformed_ledger = self.root / "malformed-lineage-ledger"
        malformed_policy = self.root / "malformed-lineage-policy.json"
        self._write_json(malformed_policy, self._policy(lineage="not a valid lineage"))
        with self.assertRaises(SessionError) as raised:
            loop_guard.init(str(malformed_ledger), str(malformed_policy))
        self.assertEqual(raised.exception.code, "INVALID_IDENTIFIER")

    def test_blocked_v1_dependency_and_candidate_prerequisite_do_not_prepare(self):
        blocked_root = self.root / "blocked-v1-task"
        blocked_root.mkdir(parents=True)
        blocked = SessionFixture(blocked_root, task_id="task-blocked-v1")
        blocked.request["dependencies"] = [{
            "id": "blocked-branch", "status": "BLOCKED",
            "reason": "Required prerequisite has not been met.", "required": True,
        }]
        blocked.write_json(blocked.request_path, blocked.request)
        blocked.create()
        self.fx = blocked
        prerequisite = {"id": "blocked-branch", "state": "BLOCKED", "evidence": []}
        candidate, _ = self._candidate(attempt="blocked-attempt", prerequisites=[prerequisite])
        report = loop_guard.check(str(self.ledger), self.head, str(candidate))
        self.assertEqual(report["status"], "WAIT_EVIDENCE")
        self.assertIn("blocked-branch", report["gaps"])
        with self.assertRaises(SessionError) as raised:
            loop_guard.prepare(str(self.ledger), self.head, str(candidate))
        self.assertEqual(raised.exception.code, "GUARD_STOP")
        omitted, _ = self._candidate(attempt="omitted-prerequisite", prerequisites=[])
        omitted_report = loop_guard.check(str(self.ledger), self.head, str(omitted))
        self.assertEqual(omitted_report["status"], "WAIT_EVIDENCE")
        self.assertIn("dependency:blocked-branch", omitted_report["gaps"])

    def test_partial_event_manifest_failure_and_lock_fail_closed(self):
        candidate, _ = self._candidate()
        atomic = loop_guard.c._atomic

        def interrupted(path, raw):
            if Path(path).name == 'manifest.json':
                raise SessionError('IO_ERROR', 'Interruption before manifest publication')
            return atomic(path, raw)

        with mock.patch.object(loop_guard.c, '_atomic', side_effect=interrupted):
            with self.assertRaises(SessionError):
                loop_guard.prepare(self.ledger, self.head, candidate)
        self.assertTrue((self.ledger / '00000002/event.json').exists())
        self.assertFalse((self.ledger / '00000002/manifest.json').exists())
        with self.assertRaises(SessionError):
            loop_guard.check(self.ledger, self.head, candidate)

        lock = self.ledger / '.lock'
        lock.write_bytes(b'crash-left-lock')
        with self.assertRaises(SessionError) as raised:
            loop_guard.check(self.ledger, self.head, candidate)
        self.assertEqual(raised.exception.code, 'LEDGER_LOCKED')

    def test_new_source_revision_does_not_consume_stale_historical_sources(self):
        self.fx.prepare('attempt-01')
        observed, _, _ = self._record_observation(attempt='attempt-01')
        (self.fx.source_dir / 'input.txt').write_bytes(b'admitted revision two\n')
        newer_root = self.root / 'revision-two'
        newer_root.mkdir()
        newer = SessionFixture(newer_root, task_id='revised-task')
        (newer.source_dir / 'input.txt').write_bytes(b'admitted revision two\n')
        newer.request['inputs'][0]['revision'] = 'r2'
        newer.write_json(newer.request_path, newer.request)
        newer.create()
        evidence = self._evidence('source-delta.txt', b'reviewed relevant source correction\n')
        candidate, _ = self._candidate(fixture=newer, attempt='retry-new-revision',
                       previous=observed['head'], goal_revision='goal-r2',
                       progress={'kind': 'SOURCE_CHANGE', 'note': 'New source revision requires relevance review.',
                                 'evidence': [evidence]})
        pending = loop_guard.check(self.ledger, self.head, candidate)
        self.assertEqual(pending['status'], 'WAIT_PROGRESS_REVIEW')
        record = {'schema': 'orchestrator.loop-review.v1', 'lineage_id': 'lineage-contract',
                  'prior_head': self.head, 'candidate_sha256': pending['candidate_sha256'],
                  'previous_observation': observed['head'], 'reviewer': 'root-review', 'producer': 'source-editor',
                  'provenance': 'Synthetic bound review of admitted revision', 'verdict': 'RELEVANT_PROGRESS',
                  'evidence': [evidence], 'rationale': 'Relevant source correction, not a hash-only assertion.'}
        review_file = self.root / 'revision-review.json'
        self._write_json(review_file, record)
        reviewed = loop_guard.review(self.ledger, self.head, review_file)
        ready = loop_guard.check(self.ledger, reviewed['head'], candidate, root_review=reviewed['head'])
        self.assertEqual(ready['status'], 'BOUNDED_RETRY_CANDIDATE')

    def test_unrelated_delta_and_no_progress_review_never_self_allow(self):
        self.fx.prepare('attempt-01')
        observed, _, _ = self._record_observation(attempt='attempt-01')
        unrelated = self._evidence('unrelated.txt', b'changed meeting timestamp\n')
        candidate, _ = self._candidate(attempt='attempt-02', previous=observed['head'],
                       progress={'kind': 'SOURCE_CHANGE', 'note': 'Caller self-claimed progress.',
                                 'evidence': [unrelated]})
        pending = loop_guard.check(self.ledger, self.head, candidate)
        self.assertEqual(pending['status'], 'WAIT_PROGRESS_REVIEW')
        record = {'schema': 'orchestrator.loop-review.v1', 'lineage_id': 'lineage-contract',
                  'prior_head': self.head, 'candidate_sha256': pending['candidate_sha256'],
                  'previous_observation': observed['head'], 'reviewer': 'root-review', 'producer': 'caller',
                  'provenance': 'Synthetic review rejects irrelevant evidence', 'verdict': 'NO_PROGRESS',
                  'evidence': [unrelated], 'rationale': 'Meeting timestamp does not repair artifact failure.'}
        review_file = self.root / 'irrelevant-review.json'
        self._write_json(review_file, record)
        reviewed = loop_guard.review(self.ledger, self.head, review_file)
        stopped = loop_guard.check(self.ledger, reviewed['head'], candidate, root_review=reviewed['head'])
        self.assertEqual(stopped['status'], 'STOP_NO_PROGRESS')

    def test_partial_prepare_failure_keeps_reservation_and_spends_budget(self):
        ledger = self.root / "partial-ledger"
        policy = self.root / "partial-policy.json"
        self._write_json(policy, self._policy(max_attempts=1))
        head = loop_guard.init(str(ledger), str(policy))["head"]
        candidate, _ = self._candidate(attempt="partial-attempt")
        with mock.patch.object(loop_guard.c, "prepare_work",
                               side_effect=SessionError("IO_ERROR", "synthetic prepare interruption")):
            failed = loop_guard.prepare(str(ledger), head, str(candidate))
        self.assertEqual(failed["status"], "PREPARE_FAILED_RESERVED")
        self.assertTrue(failed["reservation_consumed"])
        self.assertEqual(failed["used_attempts"], 1)
        retry, _ = self._candidate(attempt="after-partial-failure")
        stopped = loop_guard.check(str(ledger), failed["head"], str(retry))
        self.assertEqual(stopped["status"], "STOP_BUDGET")

    def test_stale_review_cannot_be_replayed_after_ledger_head_advances(self):
        self.fx.prepare("attempt-01")
        observed, _, _ = self._record_observation(attempt="attempt-01")
        evidence = self._evidence("stale-review-evidence.txt")
        progress = {"kind": "PREREQUISITE_PROVEN", "note": "Pinned evidence supports the declared delta.",
                    "evidence": [evidence]}
        candidate, _ = self._candidate(attempt="attempt-02", previous=observed["head"], progress=progress)
        pending = loop_guard.check(str(self.ledger), self.head, str(candidate))
        review = {
            "schema": "orchestrator.loop-review.v1", "lineage_id": "lineage-contract",
            "prior_head": self.head, "candidate_sha256": pending["candidate_sha256"],
            "previous_observation": observed["head"], "reviewer": "root-reviewer",
            "producer": "local-producer", "provenance": "independent local evidence inspection",
            "verdict": "RELEVANT_PROGRESS", "evidence": [evidence],
            "rationale": "The delta is relevant within this bounded fixture.",
        }
        review_path = self.root / "stale-review.json"
        self._write_json(review_path, review)
        reviewed = loop_guard.review(str(self.ledger), self.head, str(review_path))
        stale_review_head = reviewed["head"]
        self.head = stale_review_head

        self.fx.prepare("other-branch-attempt")
        self._record_observation(attempt="other-branch-attempt", operation="write", resource="other-resource")
        with self.assertRaises(SessionError) as raised:
            loop_guard.check(str(self.ledger), self.head, str(candidate), root_review=stale_review_head)
        self.assertEqual(raised.exception.code, "BINDING_MISMATCH")

    def test_new_independent_lineage_can_make_its_own_initial_candidate(self):
        ledger = self.root / "independent-lineage-ledger"
        policy = self.root / "independent-lineage-policy.json"
        self._write_json(policy, self._policy(lineage="lineage-independent"))
        head = loop_guard.init(str(ledger), str(policy))["head"]
        candidate, _ = self._candidate(attempt="independent-attempt", lineage="lineage-independent")
        report = loop_guard.check(str(ledger), head, str(candidate))
        self.assertEqual(report["status"], "INITIAL_ATTEMPT_CANDIDATE")
        self.assertEqual(report["used_attempts"], 0)

    def _trace(self, steps, hypotheses=None):
        return {"schema": "orchestrator.loop-trace.v1", "steps": steps,
                "hypotheses": [] if hypotheses is None else hypotheses}

    def _step(self, identifier, *, depends=(), status="SATISFIED", evidence=None):
        return {"id": identifier, "depends_on": list(depends), "kind": "SEMANTIC",
                "criterion": f"criterion-{identifier}", "status": status,
                "inputs": [], "outputs": [], "evidence": [] if evidence is None else [evidence]}

    def test_trace_empty_and_unresolved_intermediates_remain_unresolved(self):
        self.assertEqual(trace_review.inspect_trace(self._trace([]))["status"], "UNRESOLVED")
        ref = self._evidence("trace-unresolved.txt")
        trace = self._trace([self._step("unknown", status="UNKNOWN"),
                             self._step("later-failure", depends=("unknown",), status="VIOLATED", evidence=ref)])
        report = trace_review.inspect_trace(trace)
        self.assertEqual(report["status"], "UNRESOLVED")
        self.assertEqual(report["first_observed_violations"], [])
        self.assertIsNone(report["confirmed_root_cause"])

    def test_trace_reports_first_evidenced_violations_by_dag_ancestry_order_invariantly(self):
        ref = self._evidence("trace-failure.txt")
        base = [self._step("satisfied-root", evidence=ref),
                self._step("uncertain-independent", status="UNKNOWN"),
                self._step("failure-independent", status="VIOLATED", evidence=ref),
                self._step("failure-dependent", depends=("satisfied-root",), status="VIOLATED", evidence=ref)]
        reordered = [base[0], base[2], base[1], base[3]]
        reports = [trace_review.inspect_trace(self._trace(base)),
                   trace_review.inspect_trace(self._trace(reordered))]
        for report in reports:
            self.assertEqual(report["status"], "FIRST_OBSERVED_VIOLATION")
            self.assertEqual(report["first_observed_violations"],
                             ["failure-dependent", "failure-independent"])
            self.assertIsNone(report["first_observed_violation"])
            self.assertIsNone(report["confirmed_root_cause"])

    def test_trace_requires_topological_dependencies_and_exact_integer_byte_count(self):
        ref = self._evidence("trace-invalid.txt")
        invalid_order = self._trace([
            self._step("child", depends=("parent",), status="VIOLATED", evidence=ref),
            self._step("parent", evidence=ref),
        ])
        with self.assertRaises(SessionError) as raised:
            trace_review.inspect_trace(invalid_order)
        self.assertEqual(raised.exception.code, "INVALID_SCHEMA")

        bool_bytes = dict(ref, bytes=True)
        with self.assertRaises(SessionError) as raised:
            trace_review.inspect_trace(self._trace([
                self._step("step", status="VIOLATED", evidence=bool_bytes),
            ]))
        self.assertEqual(raised.exception.code, "INVALID_SCHEMA")

    def test_trace_preserves_counterevidence_and_never_confirms_cause(self):
        evidence = self._evidence("trace-support.txt")
        counter = self._evidence("trace-counter.txt", b"counterevidence\n")
        hypothesis = {"claim": "The first observed failure caused the output mismatch.",
                      "supporting_steps": ["failed-step"], "counterevidence": [counter],
                      "uncertainty": "Unverified attribution hypothesis."}
        report = trace_review.inspect_trace(self._trace([
            self._step("failed-step", status="VIOLATED", evidence=evidence),
        ], [hypothesis]))
        self.assertEqual(report["attribution_hypotheses"][0]["counterevidence"], [counter])
        self.assertIsNone(report["confirmed_root_cause"])


if __name__ == "__main__":
    unittest.main()
