from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Paper:
    title: str
    authors: list[str]
    abstract: str
    arxiv_id: str
    arxiv_url: str
    pdf_url: str | None
    published_date: str
    year: int
    month: str
    category: str
    code_url: str | None = None

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "authors": self.authors,
            "abstract": self.abstract,
            "arxiv_id": self.arxiv_id,
            "arxiv_url": self.arxiv_url,
            "pdf_url": self.pdf_url,
            "published_date": self.published_date,
            "year": self.year,
            "month": self.month,
            "category": self.category,
            "code_url": self.code_url,
        }
