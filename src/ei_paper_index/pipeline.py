from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from .arxiv_client import ArxivClient
from .processor import PaperProcessor
from .renderer import IndexRenderer


def run_pipeline(days: int, max_results: int, readme_path: Path, json_output_path: Path) -> int:
    client = ArxivClient()
    processor = PaperProcessor()
    renderer = IndexRenderer()

    papers = client.fetch_recent(max_results=max_results)
    relevant = processor.filter_recent_and_relevant(papers, days=days)
    categorized = processor.categorize(relevant)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    markdown = renderer.render_markdown(categorized, generated_at=generated_at)
    renderer.update_readme(readme_path, markdown)
    renderer.write_json(json_output_path, categorized)

    print(f"Fetched: {len(papers)}")
    print(f"Relevant (last {days} day(s)): {len(relevant)}")
    print(f"Updated README: {readme_path}")
    print(f"Updated JSON: {json_output_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build embodied intelligence paper index from arXiv")
    parser.add_argument("--days", type=int, default=1, help="Only include papers updated in the last N days")
    parser.add_argument("--max-results", type=int, default=250, help="Number of arXiv entries to fetch")
    parser.add_argument("--readme-path", type=Path, default=Path("ReadMe.md"), help="README output path")
    parser.add_argument(
        "--json-output",
        type=Path,
        default=Path("data/latest_papers.json"),
        help="JSON output path",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return run_pipeline(
        days=args.days,
        max_results=args.max_results,
        readme_path=args.readme_path,
        json_output_path=args.json_output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
