from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from .config import README_BEGIN_MARKER, README_END_MARKER
from .models import CategorizedPaper


class IndexRenderer:
    def render_markdown(self, papers: list[CategorizedPaper], generated_at: str) -> str:
        grouped = defaultdict(list)
        for item in papers:
            for topic in item.topics:
                grouped[topic].append(item)

        lines: list[str] = []
        lines.append(f"## Daily Embodied Intelligence Paper Index ({generated_at} UTC)")
        lines.append("")
        lines.append(f"Total papers: **{len(papers)}**")
        lines.append("")

        for topic in sorted(grouped.keys()):
            lines.append(f"### {topic}")
            lines.append("")
            for item in grouped[topic]:
                p = item.paper
                authors = ", ".join(p.authors[:5])
                if len(p.authors) > 5:
                    authors += ", et al."
                lines.append(f"- [{p.title}]({p.arxiv_url})")
                lines.append(f"  - Authors: {authors}")
                lines.append(f"  - Published: {p.published.date().isoformat()}")
                lines.append(f"  - Categories: {', '.join(p.categories)}")
                if p.pdf_url:
                    lines.append(f"  - PDF: [link]({p.pdf_url})")
                if item.code_links:
                    code_items = " | ".join(f"[code]({url})" for url in item.code_links)
                    lines.append(f"  - Code Links: {code_items}")
            lines.append("")

        return "\n".join(lines).rstrip() + "\n"

    def update_readme(self, readme_path: Path, section_markdown: str) -> None:
        if readme_path.exists():
            original = readme_path.read_text(encoding="utf-8")
        else:
            original = ""

        scaffold = self._ensure_scaffold(original)
        start = scaffold.index(README_BEGIN_MARKER) + len(README_BEGIN_MARKER)
        end = scaffold.index(README_END_MARKER)
        updated = scaffold[:start] + "\n\n" + section_markdown + "\n" + scaffold[end:]
        readme_path.write_text(updated, encoding="utf-8")

    def write_json(self, output_path: Path, papers: list[CategorizedPaper]) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        payload = []
        for item in papers:
            paper = item.paper
            payload.append(
                {
                    "id": paper.id,
                    "title": paper.title,
                    "summary": paper.summary,
                    "authors": paper.authors,
                    "published": paper.published.isoformat(),
                    "updated": paper.updated.isoformat(),
                    "arxiv_url": paper.arxiv_url,
                    "pdf_url": paper.pdf_url,
                    "categories": paper.categories,
                    "topics": item.topics,
                    "code_links": item.code_links,
                }
            )
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def _ensure_scaffold(content: str) -> str:
        if README_BEGIN_MARKER in content and README_END_MARKER in content:
            return content

        header = "# Embodied Intelligence Paper Index\n\n"
        intro = (
            "Automatically updated daily from arXiv for embodied intelligence research.\n\n"
            "This repository tracks recent papers and detected code links.\n\n"
        )
        markers = f"{README_BEGIN_MARKER}\n{README_END_MARKER}\n"
        if content.strip():
            return content.rstrip() + "\n\n" + markers
        return header + intro + markers
