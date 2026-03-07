from __future__ import annotations

from .arxiv import fetch_recent_arxiv_papers
from .config import CATEGORIES_DIR, DATA_PATH, README_PATH
from .database import update_paper_database
from .markdown import generate_category_files, generate_readme


def run_daily_pipeline(days: int = 1, max_results: int = 500) -> dict:
    fresh = fetch_recent_arxiv_papers(days=days, max_results=max_results)
    all_papers = update_paper_database(fresh, DATA_PATH)
    readme_content = generate_readme(all_papers, README_PATH)
    category_files = generate_category_files(all_papers, CATEGORIES_DIR)
    return {
        "fetched": len(fresh),
        "total_in_db": len(all_papers),
        "readme_bytes": len(readme_content.encode("utf-8")),
        "category_files": len(category_files),
    }
