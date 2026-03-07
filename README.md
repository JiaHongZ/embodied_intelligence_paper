# Embodied Intelligence Papers

Automatically updated daily.

This repository tracks new Embodied Intelligence papers from arXiv, stores all papers in `data/papers.json`, and renders fast markdown views for latest and archived papers.

## Pipeline

1. Fetch recent arXiv papers (`scripts/fetch_arxiv.py`)
2. Categorize papers (`scripts/categorize.py`)
3. Merge into JSON database with deduplication by `arxiv_id` (`scripts/update_database.py`)
4. Generate latest README view (`scripts/generate_readme.py`)
5. Generate yearly category files (`scripts/generate_categories.py`)

Or run everything in one command:

```bash
python scripts/run_daily.py --days 1 --max-results 500
```

## Latest Papers (Last 7 Days)

No new papers found in the last 7 days.

## Full Archive

### 2026

- Embodied Foundation Models -> [categories/2026/foundation_models.md](categories/2026/foundation_models.md)
- Robot Manipulation -> [categories/2026/manipulation.md](categories/2026/manipulation.md)
- Robot Navigation -> [categories/2026/navigation.md](categories/2026/navigation.md)
- Vision-Language-Action -> [categories/2026/vla.md](categories/2026/vla.md)
- Embodied Agents -> [categories/2026/embodied_agents.md](categories/2026/embodied_agents.md)
- Simulation and Sim2Real -> [categories/2026/sim2real.md](categories/2026/sim2real.md)
- Human-Robot Interaction -> [categories/2026/hri.md](categories/2026/hri.md)
- Other -> [categories/2026/other.md](categories/2026/other.md)

### 2025

- Embodied Foundation Models -> [categories/2025/foundation_models.md](categories/2025/foundation_models.md)
- Robot Manipulation -> [categories/2025/manipulation.md](categories/2025/manipulation.md)
- Robot Navigation -> [categories/2025/navigation.md](categories/2025/navigation.md)
- Vision-Language-Action -> [categories/2025/vla.md](categories/2025/vla.md)
- Embodied Agents -> [categories/2025/embodied_agents.md](categories/2025/embodied_agents.md)
- Simulation and Sim2Real -> [categories/2025/sim2real.md](categories/2025/sim2real.md)
- Human-Robot Interaction -> [categories/2025/hri.md](categories/2025/hri.md)
- Other -> [categories/2025/other.md](categories/2025/other.md)
