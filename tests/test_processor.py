from datetime import datetime, timezone

from ei_paper_index.models import ArxivPaper
from ei_paper_index.processor import PaperProcessor


def build_paper(title: str, summary: str, updated: datetime) -> ArxivPaper:
    return ArxivPaper(
        id="id",
        title=title,
        summary=summary,
        authors=["A"],
        published=updated,
        updated=updated,
        arxiv_url="https://arxiv.org/abs/1234.5678",
        pdf_url=None,
        categories=["cs.RO"],
    )


def test_filters_keyword_and_date() -> None:
    now = datetime(2026, 3, 7, 10, 0, tzinfo=timezone.utc)
    processor = PaperProcessor(now_utc=now)

    keep = build_paper("Embodied robot navigation", "Good paper", now.replace(tzinfo=None))
    old = build_paper("Embodied robot navigation", "Old", datetime(2026, 2, 20, 10, 0))
    irrelevant = build_paper("Graph theory", "No robotics", now.replace(tzinfo=None))

    out = processor.filter_recent_and_relevant([keep, old, irrelevant], days=2)
    assert len(out) == 1
    assert out[0].title == keep.title


def test_categorizes_vla_and_manipulation() -> None:
    processor = PaperProcessor(now_utc=datetime(2026, 3, 7, tzinfo=timezone.utc))
    paper = build_paper(
        "A Vision-Language-Action model for dexterous manipulation",
        "We propose a VLA approach for robot manipulation.",
        datetime(2026, 3, 7, 10, 0),
    )

    result = processor.categorize([paper])[0]
    assert "Vision-Language-Action" in result.topics
    assert "Robot Manipulation" in result.topics
