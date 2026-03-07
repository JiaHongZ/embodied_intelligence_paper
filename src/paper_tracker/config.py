from __future__ import annotations

from pathlib import Path

ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_SEARCH_CATEGORIES = ["cs.AI", "cs.RO", "cs.CV", "cs.LG", "cs.CL", "stat.ML"]
KEYWORD_FILTER = [
    "embodied",
    "robot",
    "robotics",
    "manipulation",
    "navigation",
    "locomotion",
    "grasp",
    "humanoid",
    "vision-language-action",
    "vla",
    "embodied agent",
]

FIELD_RULES: dict[str, list[str]] = {
    "Embodied Foundation Models": ["foundation model", "generalist", "world model", "pretrain", "pre-trained"],
    "Robot Manipulation": ["manipulation", "grasp", "dexterous", "pick", "place"],
    "Robot Navigation": ["navigation", "path planning", "slam", "locomotion", "mobile robot"],
    "Vision-Language-Action": ["vision-language-action", "vla", "vision language action", "vlm"],
    "Embodied Agents": ["embodied agent", "agentic", "interactive agent", "agent"],
    "Simulation and Sim2Real": ["sim2real", "sim-to-real", "simulation-to-real", "domain randomization", "simulator"],
    "Human-Robot Interaction": ["human-robot", "hri", "human robot", "social robot"],
}

FALLBACK_FIELD = "Other"

FIELD_TO_FILE = {
    "Embodied Foundation Models": "foundation_models.md",
    "Robot Manipulation": "manipulation.md",
    "Robot Navigation": "navigation.md",
    "Vision-Language-Action": "vla.md",
    "Embodied Agents": "embodied_agents.md",
    "Simulation and Sim2Real": "sim2real.md",
    "Human-Robot Interaction": "hri.md",
    "Other": "other.md",
}

ROOT = Path(".")
DATA_PATH = ROOT / "data" / "papers.json"
README_PATH = ROOT / "README.md"
CATEGORIES_DIR = ROOT / "categories"
