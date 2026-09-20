from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Experience:
    frame: int
    state: tuple[float, ...]
    action: str
    reward: int
    next_state: tuple[float, ...]
    done: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "frame": self.frame,
            "state": list(self.state),
            "action": self.action,
            "reward": self.reward,
            "next_state": list(self.next_state),
            "done": self.done,
        }
