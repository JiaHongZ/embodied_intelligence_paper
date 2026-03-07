from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.arxiv import fetch_recent_arxiv_papers


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch recent embodied intelligence papers from arXiv")
    parser.add_argument("--days", type=int, default=1)
    parser.add_argument("--max-results", type=int, default=500)
    parser.add_argument("--output", default="data/new_papers.json")
    args = parser.parse_args()

    papers = fetch_recent_arxiv_papers(days=args.days, max_results=args.max_results)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)

    print(f"Fetched {len(papers)} papers to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
