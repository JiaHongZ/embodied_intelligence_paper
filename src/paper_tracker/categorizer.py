from __future__ import annotations

import re
from bs4 import BeautifulSoup

from .config import FALLBACK_FIELD, FIELD_RULES

URL_RE = re.compile(r"https?://[^\s\]\)\"']+", re.IGNORECASE)
GITHUB_RE = re.compile(r"https?://(?:www\.)?github\.com/[^\s\]\)\"']+", re.IGNORECASE)


def extract_github_link(abstract: str) -> str | None:
    text = BeautifulSoup(abstract or "", "html.parser").get_text(" ", strip=True)
    match = GITHUB_RE.search(text)
    if match:
        return match.group(0).rstrip(".,;)")
    for url in URL_RE.findall(text):
        if "github.com" in url.lower():
            return url.rstrip(".,;)")
    return None


def categorize_paper(paper: dict) -> str:
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    for field, keywords in FIELD_RULES.items():
        if any(keyword in text for keyword in keywords):
            return field
    return FALLBACK_FIELD
