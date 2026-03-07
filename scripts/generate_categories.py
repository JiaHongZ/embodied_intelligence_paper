from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.markdown import generate_category_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate yearly category markdown archives")
    parser.add_argument("--database", default="data/papers.json")
    parser.add_argument("--output-dir", default="categories")
    args = parser.parse_args()

    papers = json.loads(Path(args.database).read_text(encoding="utf-8")) if Path(args.database).exists() else []
    files = generate_category_files(papers, Path(args.output_dir))
    print(f"Category files updated: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
