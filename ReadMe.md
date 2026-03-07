# Embodied Intelligence Paper Index

Automatically updated daily from arXiv for embodied intelligence research.

## What This Project Does

- Fetches recent papers from arXiv (`cs.AI`, `cs.RO`, `cs.CV`, `cs.LG`, `cs.CL`, `stat.ML`)
- Filters by embodied intelligence keywords
- Categorizes papers into major subfields
- Extracts potential code links from abstracts
- Updates this README and `data/latest_papers.json`
- Runs daily via GitHub Actions

## Local Usage

```bash
python -m pip install -e .
python -m ei_paper_index --days 1 --max-results 300 --readme-path ReadMe.md --json-output data/latest_papers.json
```

## GitHub Actions

The workflow file is located at `.github/workflows/daily_update.yml`.

It runs once per day at `01:00 UTC` and can also be triggered manually using `workflow_dispatch`.

<!-- PAPER_INDEX_START -->
<!-- PAPER_INDEX_END -->
