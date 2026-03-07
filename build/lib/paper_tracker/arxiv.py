from __future__ import annotations

from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode

import feedparser
import requests
from tqdm import tqdm

from .config import ARXIV_API_URL, ARXIV_SEARCH_CATEGORIES, KEYWORD_FILTER


def fetch_recent_arxiv_papers(days: int, max_results: int) -> list[dict]:
    query = " OR ".join(f"cat:{cat}" for cat in ARXIV_SEARCH_CATEGORIES)
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API_URL}?{urlencode(params)}"
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    feed = feedparser.parse(response.text)
    threshold = datetime.now(timezone.utc) - timedelta(days=days)

    papers: list[dict] = []
    for entry in tqdm(feed.entries, desc="Processing arXiv entries", unit="paper"):
        updated = _safe_parse_datetime(entry.get("updated", ""))
        if updated and updated < threshold:
            continue

        title = _clean(entry.get("title", ""))
        abstract = _clean(entry.get("summary", ""))
        text = f"{title} {abstract}".lower()
        if not any(keyword in text for keyword in KEYWORD_FILTER):
            continue

        arxiv_id = _extract_arxiv_id(entry.get("id", ""))
        authors = [a.get("name", "").strip() for a in entry.get("authors", []) if a.get("name")]

        pdf_url = None
        for link in entry.get("links", []):
            if link.get("type") == "application/pdf":
                pdf_url = link.get("href")

        published = _safe_parse_datetime(entry.get("published", "")) or updated
        if not published:
            continue

        categories = [tag.get("term", "") for tag in entry.get("tags", []) if tag.get("term")]

        papers.append(
            {
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "arxiv_id": arxiv_id,
                "arxiv_url": entry.get("id", ""),
                "pdf_url": pdf_url,
                "published_date": published.date().isoformat(),
                "year": published.year,
                "month": published.strftime("%B"),
                "source_categories": categories,
            }
        )

    return papers


def _safe_parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            dt = datetime.strptime(value, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue
    return None


def _extract_arxiv_id(url: str) -> str:
    if "/abs/" in url:
        return url.rsplit("/abs/", 1)[-1]
    return url.rsplit("/", 1)[-1]


def _clean(text: str) -> str:
    return " ".join(text.split())
