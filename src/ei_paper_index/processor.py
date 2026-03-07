from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

from .config import DEFAULT_FALLBACK_TOPIC, KEYWORDS, TOPIC_KEYWORDS
from .models import ArxivPaper, CategorizedPaper

URL_PATTERN = re.compile(r"https?://[^\s\]\)\"']+")


class PaperProcessor:
    def __init__(self, now_utc: datetime | None = None) -> None:
        self.now_utc = now_utc or datetime.now(timezone.utc)

    def filter_recent_and_relevant(self, papers: list[ArxivPaper], days: int = 1) -> list[ArxivPaper]:
        threshold = self.now_utc - timedelta(days=days)
        out: list[ArxivPaper] = []
        for paper in papers:
            updated_utc = paper.updated.replace(tzinfo=timezone.utc)
            if updated_utc < threshold:
                continue
            haystack = f"{paper.title} {paper.summary}".lower()
            if any(keyword in haystack for keyword in KEYWORDS):
                out.append(paper)
        return out

    def categorize(self, papers: list[ArxivPaper]) -> list[CategorizedPaper]:
        categorized: list[CategorizedPaper] = []
        for paper in papers:
            text = f"{paper.title} {paper.summary}".lower()
            topics = [
                topic
                for topic, topic_keywords in TOPIC_KEYWORDS.items()
                if any(keyword in text for keyword in topic_keywords)
            ]
            if not topics:
                topics = [DEFAULT_FALLBACK_TOPIC]
            code_links = self.extract_links(paper.summary)
            categorized.append(CategorizedPaper(paper=paper, topics=topics, code_links=code_links))
        return categorized

    @staticmethod
    def extract_links(text: str) -> list[str]:
        links = URL_PATTERN.findall(text)
        seen: set[str] = set()
        unique: list[str] = []
        for link in links:
            clean = link.rstrip(".,;)")
            if clean not in seen:
                seen.add(clean)
                unique.append(clean)
        return unique
