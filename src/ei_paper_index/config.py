from __future__ import annotations

ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_CATEGORIES = ["cs.AI", "cs.RO", "cs.CV", "cs.LG", "cs.CL", "stat.ML"]

KEYWORDS = [
    "embodied",
    "robot",
    "robotics",
    "manipulation",
    "navigation",
    "vision-language-action",
    "vla",
    "embodied agent",
]

TOPIC_KEYWORDS: dict[str, list[str]] = {
    "Embodied AI": ["embodied ai", "embodied intelligence", "embodied"],
    "Embodied Agents": ["embodied agent", "agentic robot", "embodied agents"],
    "Robotics Learning": ["robot learning", "learning for robotics", "policy learning"],
    "Vision-Language-Action": ["vision-language-action", "vla", "vlm", "multimodal action"],
    "Robot Manipulation": ["manipulation", "grasp", "pick and place", "dexterous"],
    "Robot Navigation": ["navigation", "path planning", "slam", "locomotion"],
    "Multimodal Robotics": ["multimodal", "vision-language", "language-conditioned"],
    "Foundation Models for Robotics": ["foundation model", "generalist", "large model", "world model"],
    "Reinforcement Learning for Robotics": ["reinforcement learning", "rl", "policy optimization"],
    "Simulation-to-Real Transfer": ["sim-to-real", "simulation-to-real", "domain randomization"],
    "Human-Robot Interaction": ["human-robot interaction", "hri", "human robot"],
}

DEFAULT_FALLBACK_TOPIC = "Other Embodied Intelligence"
README_BEGIN_MARKER = "<!-- PAPER_INDEX_START -->"
README_END_MARKER = "<!-- PAPER_INDEX_END -->"
