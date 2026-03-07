from __future__ import annotations

from datetime import datetime
from typing import Iterable
from xml.etree import ElementTree as ET

import requests

from .config import ARXIV_API_URL, ARXIV_CATEGORIES
from .models import ArxivPaper

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


class ArxivClient:
    def __init__(self, base_url: str = ARXIV_API_URL, timeout: int = 30) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def fetch_recent(self, max_results: int = 200) -> list[ArxivPaper]:
        query = " OR ".join(f"cat:{category}" for category in ARXIV_CATEGORIES)
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        response = requests.get(self.base_url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return list(self._parse_feed(response.text))

    def _parse_feed(self, xml_text: str) -> Iterable[ArxivPaper]:
        root = ET.fromstring(xml_text)
        for entry in root.findall("atom:entry", ATOM_NS):
            paper_id = _get_text(entry, "atom:id")
            title = _normalize(_get_text(entry, "atom:title"))
            summary = _normalize(_get_text(entry, "atom:summary"))
            published = _parse_date(_get_text(entry, "atom:published"))
            updated = _parse_date(_get_text(entry, "atom:updated"))
            authors = [
                _normalize(author.findtext("atom:name", default="", namespaces=ATOM_NS))
                for author in entry.findall("atom:author", ATOM_NS)
            ]
            links = entry.findall("atom:link", ATOM_NS)
            pdf_url = None
            arxiv_url = paper_id
            for link in links:
                href = link.attrib.get("href")
                title_attr = link.attrib.get("title", "")
                rel = link.attrib.get("rel", "")
                if rel == "alternate" and href:
                    arxiv_url = href
                if title_attr == "pdf" and href:
                    pdf_url = href
            categories = [c.attrib.get("term", "") for c in entry.findall("atom:category", ATOM_NS)]
            yield ArxivPaper(
                id=paper_id,
                title=title,
                summary=summary,
                authors=[a for a in authors if a],
                published=published,
                updated=updated,
                arxiv_url=arxiv_url,
                pdf_url=pdf_url,
                categories=[c for c in categories if c],
            )


def _get_text(entry: ET.Element, path: str) -> str:
    value = entry.findtext(path, default="", namespaces=ATOM_NS)
    return value.strip()


def _parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def _normalize(value: str) -> str:
    return " ".join(value.split())
