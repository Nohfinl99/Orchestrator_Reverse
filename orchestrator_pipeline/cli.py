"""One explicit local caller; output is a JSON receipt, never model/tool dispatch."""
import argparse
import json
from .core import PipelineError, prepare


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise PipelineError("INVALID_ARGUMENTS", message)


def main(argv=None):
    parser = Parser(description=__doc__)
    parser.add_argument("--input", required=True, help="Operator-selected request JSON file")
    parser.add_argument("--output-root", required=True, help="Local run storage; choose outside public repo")
    parser.add_argument("--run-id", required=True, help="New immutable run ID")
    parser.add_argument("--proposal-file", help="Optional UTF-8 proposed text; never applied implicitly")
    parser.add_argument("--accept-proposal-digest", help="Exact proposal bundle digest; operator annotation only")
    parser.add_argument("--resume-from", help="Existing run ID in the same output-root")
    try:
        args = parser.parse_args(argv)
        result, code = prepare(args.input, args.output_root, args.run_id,
                               proposal_path=args.proposal_file, accept_digest=args.accept_proposal_digest,
                               resume_from=args.resume_from)
    except PipelineError as exc:
        result, code = {"status": "INVALID_INPUT", "code": exc.code, "error": str(exc),
                        "execution_authorized": False}, 2
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return code
