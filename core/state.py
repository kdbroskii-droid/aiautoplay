from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AgentState:
    frame: int = 0
    episode: int = 0
    running: bool = True
    last_action: str = "wait"
    reward: int = 0
