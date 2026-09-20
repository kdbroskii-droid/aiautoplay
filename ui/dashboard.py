from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Dashboard:
    """Minimal terminal dashboard for sandbox training metrics."""

    def render(self, *, frame: int, action: str, reward: int, average_reward: float) -> str:
        label = {1: "GREEN", 0: "ORANGE", -1: "RED"}[reward]
        return f"frame={frame:04d} action={action:<12} {label:<6} reward={reward:+d} avg={average_reward:+.3f}"
