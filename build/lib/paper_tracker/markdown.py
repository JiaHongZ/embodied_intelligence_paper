from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from .config import FIELD_TO_FILE


def generate_readme(papers: list[dict], output_path: Path) -> str:
    now = datetime.utcnow().date()
    window_start = now - timedelta(days=7)

    rows = []
    for paper in papers:
        try:
            published = datetime.strptime(paper["published_date"], "%Y-%m-%d").date()
        except (KeyError, ValueError, TypeError):
            continue
        if published >= window_start:
            enriched = dict(paper)
            enriched["published"] = published
            rows.append(enriched)

    lines: list[str] = []
    lines.append("# Embodied Intelligence Papers")
    lines.append("")
    lines.append("Automatically updated daily.")
    lines.append("")
    lines.append("## Latest Papers (Last 7 Days)")
    lines.append("")

    if rows:
        frame = pd.DataFrame(rows).sort_values(by="published", ascending=False)
        for field in FIELD_TO_FILE.keys():
            subset = frame[frame["category"] == field]
            if subset.empty:
                continue
            lines.append(f"### {field}")
            lines.append("")
            for _, row in subset.iterrows():
                lines.append(f"- [{row['title']}]({row['arxiv_url']})")
                lines.append(f"  {', '.join(row['authors'])}")
                if row.get("code_url"):
                    lines.append(f"  Code: {row['code_url']}")
            lines.append("")
    else:
        lines.append("No new papers found in the last 7 days.")
        lines.append("")

    lines.append("## Full Archive")
    lines.append("")

    years = _discover_years(papers, output_path.parent / "categories")
    for year in years:
        lines.append(f"### {year}")
        lines.append("")
        for field, file_name in FIELD_TO_FILE.items():
            path = f"categories/{year}/{file_name}"
            lines.append(f"- {field} -> [{path}]({path})")
        lines.append("")

    content = "\n".join(lines).rstrip() + "\n"
    output_path.write_text(content, encoding="utf-8")
    return content


def generate_category_files(papers: list[dict], categories_root: Path) -> list[Path]:
    categories_root.mkdir(parents=True, exist_ok=True)

    years = sorted({int(p["year"]) for p in papers if p.get("year")}, reverse=True)
    if not years:
        current = datetime.utcnow().year
        years = [current, current - 1]

    frame = pd.DataFrame(papers) if papers else pd.DataFrame()
    created: list[Path] = []

    for year in years:
        year_dir = categories_root / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        if frame.empty:
            year_frame = pd.DataFrame()
        else:
            year_frame = frame[frame["year"].astype(int) == year]

        for field, file_name in FIELD_TO_FILE.items():
            subset = year_frame[year_frame["category"] == field].copy() if not year_frame.empty else pd.DataFrame()
            out_path = year_dir / file_name
            created.append(out_path)

            title = f"# {field} Papers ({year})"
            if subset.empty:
                out_path.write_text(title + "\n\nNo papers yet.\n", encoding="utf-8")
                continue

            subset["date_obj"] = pd.to_datetime(subset["published_date"], errors="coerce")
            subset = subset.sort_values(by="date_obj", ascending=False)

            lines = [title, ""]
            for month in subset["month"].dropna().unique():
                month_rows = subset[subset["month"] == month]
                lines.append(f"## {month}")
                lines.append("")
                for _, row in month_rows.iterrows():
                    lines.append(f"- [{row['title']}]({row['arxiv_url']})")
                    lines.append(f"  {', '.join(row['authors'])}")
                    if row.get("code_url"):
                        lines.append(f"  Code: {row['code_url']}")
                lines.append("")

            out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    return created


def _discover_years(papers: list[dict], categories_dir: Path) -> list[int]:
    from_db = {int(p["year"]) for p in papers if p.get("year")}
    from_dir = set()
    if categories_dir.exists():
        for child in categories_dir.iterdir():
            if child.is_dir() and child.name.isdigit():
                from_dir.add(int(child.name))

    years = sorted(from_db | from_dir, reverse=True)
    if years:
        return years

    current = datetime.utcnow().year
    return [current, current - 1]
