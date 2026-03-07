from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from paper_tracker.categorizer import categorize_paper, extract_github_link


def main() -> int:
    parser = argparse.ArgumentParser(description="Categorize papers and enrich with GitHub links")
    parser.add_argument("--input", default="data/new_papers.json")
    parser.add_argument("--output", default="data/categorized_papers.json")
    args = parser.parse_args()

    papers = json.loads(Path(args.input).read_text(encoding="utf-8")) if Path(args.input).exists() else []

    out = []
    for paper in papers:
        paper["category"] = categorize_paper(paper)
        paper["code_url"] = extract_github_link(paper.get("abstract", ""))
        out.append(paper)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Categorized {len(out)} papers to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
