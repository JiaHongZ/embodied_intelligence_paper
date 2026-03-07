from __future__ import annotations

import json
from pathlib import Path

from .categorizer import categorize_paper, extract_github_link
from .models import Paper


def update_paper_database(new_papers: list[dict], db_path: Path) -> list[dict]:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    existing = _read_json(db_path)
    by_id: dict[str, dict] = {item["arxiv_id"]: item for item in existing if item.get("arxiv_id")}

    for raw in new_papers:
        arxiv_id = raw.get("arxiv_id")
        if not arxiv_id:
            continue
        category = categorize_paper(raw)
        code_url = extract_github_link(raw.get("abstract", ""))
        paper = Paper(
            title=raw.get("title", "").strip(),
            authors=raw.get("authors", []),
            abstract=raw.get("abstract", "").strip(),
            arxiv_id=arxiv_id,
            arxiv_url=raw.get("arxiv_url", ""),
            pdf_url=raw.get("pdf_url"),
            published_date=raw.get("published_date", ""),
            year=int(raw.get("year", 0)),
            month=raw.get("month", ""),
            category=category,
            code_url=code_url,
        )

        if arxiv_id in by_id:
            old = by_id[arxiv_id]
            old.update(paper.to_dict())
        else:
            by_id[arxiv_id] = paper.to_dict()

    merged = sorted(by_id.values(), key=lambda x: x.get("published_date", ""), reverse=True)
    db_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    return merged


def _read_json(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
