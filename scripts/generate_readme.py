from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.markdown import generate_readme


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README with latest 7-day papers")
    parser.add_argument("--database", default="data/papers.json")
    parser.add_argument("--output", default="README.md")
    args = parser.parse_args()

    papers = json.loads(Path(args.database).read_text(encoding="utf-8")) if Path(args.database).exists() else []
    generate_readme(papers, Path(args.output))
    print(f"README updated: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
