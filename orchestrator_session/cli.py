"""Local, file-only session lifecycle commands; this CLI never dispatches tools."""
from __future__ import annotations

import argparse
import json
import sys

from .core import SessionError, check, create, prepare_work, record_result, record_review, report


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise SessionError("INVALID_ARGUMENTS", message)


def _emit(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n"
    # PowerShell/Windows consoles may use a legacy code page. Keep JSON UTF-8.
    try:
        sys.stdout.buffer.write(raw.encode("utf-8"))
        sys.stdout.buffer.flush()
    except (AttributeError, OSError):
        sys.stdout.write(raw)


def main(argv=None):
    parser = Parser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("create", help="Create an immutable task from an operator-selected JSON request")
    p.add_argument("--request", required=True, help="UTF-8 JSON request file; exact bytes are retained")
    p.add_argument("--output-root", required=True, help="Explicit local run storage outside the public repository")

    p = sub.add_parser("prepare-work", help="Create a new attempt and work packet")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--attempt-id", required=True)
    p.add_argument("--parent-attempt")
    p.add_argument("--executor", default="UNKNOWN", help="Actual executor label, or UNKNOWN")

    p = sub.add_parser("record-result", help="Record a result file for an attempt")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--attempt-id", required=True)
    p.add_argument("--result", required=True, help="Operator-selected result JSON file")

    p = sub.add_parser("record-review", help="Record a review; origin remains unauthenticated")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--attempt-id", required=True)
    p.add_argument("--review", required=True, help="Review JSON with criteria and evidence references")

    for name, func in (("check", check), ("report", report)):
        p = sub.add_parser(name, help=f"{name.capitalize()} local task artifacts mechanically")
        p.add_argument("--task-dir", required=True)
        p.add_argument("--attempt-id")

    try:
        args = parser.parse_args(argv)
        if args.command == "create":
            result = create(args.request, args.output_root)
            code = 0
        elif args.command == "prepare-work":
            result = prepare_work(args.task_dir, args.attempt_id,
                                  parent_attempt=args.parent_attempt, executor=args.executor)
            code = 0
        elif args.command == "record-result":
            result = record_result(args.task_dir, args.attempt_id, args.result)
            code = 0
        elif args.command == "record-review":
            result = record_review(args.task_dir, args.attempt_id, args.review)
            code = 0
        elif args.command == "check":
            result = check(args.task_dir, args.attempt_id)
            code = 0
        else:
            result = report(args.task_dir, args.attempt_id)
            # Incomplete/pending states are successful reports, not completion claims.
            code = 0
    except SessionError as exc:
        result, code = {"status": "ERROR", "code": exc.code, "error": str(exc)}, 2
    except (OSError, TypeError, ValueError, RecursionError) as exc:
        result, code = {"status": "ERROR", "code": type(exc).__name__, "error": str(exc)}, 2
    _emit(result)
    return code
