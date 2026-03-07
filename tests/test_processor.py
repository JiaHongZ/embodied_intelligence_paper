from __future__ import annotations

from pathlib import Path

from paper_tracker.categorizer import categorize_paper, extract_github_link
from paper_tracker.database import update_paper_database


def test_extract_github_link() -> None:
    abstract = "Code available at https://github.com/example/repo for robot manipulation."
    assert extract_github_link(abstract) == "https://github.com/example/repo"


def test_categorize_paper() -> None:
    paper = {"title": "A Vision-Language-Action Policy", "abstract": "A VLA model for robotics."}
    assert categorize_paper(paper) == "Vision-Language-Action"


def test_update_paper_database_dedup(tmp_path: Path) -> None:
    db = tmp_path / "papers.json"
    raw = [
        {
            "title": "Paper A",
            "authors": ["Alice"],
            "abstract": "robot manipulation",
            "arxiv_id": "2603.12345",
            "arxiv_url": "https://arxiv.org/abs/2603.12345",
            "pdf_url": "https://arxiv.org/pdf/2603.12345.pdf",
            "published_date": "2026-03-01",
            "year": 2026,
            "month": "March",
        }
    ]
    out1 = update_paper_database(raw, db)
    out2 = update_paper_database(raw, db)
    assert len(out1) == 1
    assert len(out2) == 1
