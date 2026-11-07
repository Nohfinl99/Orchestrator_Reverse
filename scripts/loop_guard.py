"""Standalone opt-in local loop guard; no model/tool dispatch or authority."""
from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from orchestrator_session import core, loop_guard
from orchestrator_session.cli import Parser, _emit
from orchestrator_session.trace_review import inspect_trace


def main(argv=None):
    parser = Parser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name, source in (('init', 'policy'), ('observe', 'observation'), ('review', 'review'), ('check', 'candidate'), ('prepare', 'candidate')):
        command = sub.add_parser(name)
        command.add_argument('--ledger', required=True)
        command.add_argument('--' + source, required=True)
        if name != 'init':
            command.add_argument('--expected-head', required=True)
        if name in ('check', 'prepare'):
            command.add_argument('--root-review')
        if name == 'prepare':
            command.add_argument('--executor', default='UNKNOWN')
            command.add_argument('--parent-attempt')
    command = sub.add_parser('trace-check')
    command.add_argument('--trace', required=True)
    try:
        args = parser.parse_args(argv)
        if args.command == 'trace-check':
            result = inspect_trace(core.decode(core._read(args.trace, core.MAX_JSON)))
        elif args.command == 'init':
            result = loop_guard.init(args.ledger, args.policy)
        elif args.command == 'observe':
            result = loop_guard.observe(args.ledger, args.expected_head, args.observation)
        elif args.command == 'review':
            result = loop_guard.review(args.ledger, args.expected_head, args.review)
        elif args.command == 'check':
            result = loop_guard.check(args.ledger, args.expected_head, args.candidate, args.root_review)
        else:
            result = loop_guard.prepare(args.ledger, args.expected_head, args.candidate, args.root_review,
                                        args.executor, args.parent_attempt)
        code = 2 if result['status'] == 'PREPARE_FAILED_RESERVED' else 0
    except core.SessionError as exc:
        result, code = {'status': 'ERROR', 'code': exc.code, 'error': str(exc)}, 2
    except (OSError, TypeError, ValueError, KeyError, RecursionError) as exc:
        result, code = {'status': 'ERROR', 'code': type(exc).__name__, 'error': str(exc)}, 2
    _emit(result)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
