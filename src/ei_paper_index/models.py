from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ArxivPaper:
    id: str
    title: str
    summary: str
    authors: list[str]
    published: datetime
    updated: datetime
    arxiv_url: str
    pdf_url: str | None
    categories: list[str]


@dataclass(slots=True)
class CategorizedPaper:
    paper: ArxivPaper
    topics: list[str]
    code_links: list[str]
