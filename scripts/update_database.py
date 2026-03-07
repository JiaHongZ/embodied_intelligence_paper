from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.database import update_paper_database


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge newly fetched papers into data/papers.json")
    parser.add_argument("--input", default="data/categorized_papers.json")
    parser.add_argument("--database", default="data/papers.json")
    args = parser.parse_args()

    new_papers = json.loads(Path(args.input).read_text(encoding="utf-8")) if Path(args.input).exists() else []

    merged = update_paper_database(new_papers, Path(args.database))
    print(f"Database updated: {len(merged)} total papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
