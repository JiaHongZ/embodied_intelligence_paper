from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.pipeline import run_daily_pipeline


def main() -> int:
    parser = argparse.ArgumentParser(description="Run full daily embodied intelligence paper pipeline")
    parser.add_argument("--days", type=int, default=1)
    parser.add_argument("--max-results", type=int, default=500)
    args = parser.parse_args()

    result = run_daily_pipeline(days=args.days, max_results=args.max_results)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
