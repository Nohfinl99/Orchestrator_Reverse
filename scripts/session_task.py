"""Run the public local session lifecycle caller under isolated Python."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from orchestrator_session.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
