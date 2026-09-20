from __future__ import annotations

from dataclasses import dataclass

from .events import RewardEvent, RewardEventType


@dataclass(frozen=True)
class RewardWeights:
    move: float = 0.25
    shoot: float = 0.40
    classify: float = 0.35
    build: float = 0.35
    edit: float = 0.35
    elimination: float = 1.0
    pickup: float = 0.25
    interact: float = 0.20
    target_acquired: float = 0.20
    objective_progress: float = 0.50
    standing_still: float = -0.60
    circular_movement: float = -0.50
    death: float = -1.0
    missed_action: float = -0.25


class RewardShaper:
    """Maps sandbox events to the required -1/0/+1 learning signal."""

    def __init__(self, weights: RewardWeights | None = None) -> None:
        self.weights = weights or RewardWeights()

    def raw_value(self, event: RewardEvent) -> float:
        return getattr(self.weights, event.event_type.value)

    def reward(self, event: RewardEvent) -> int:
        value = self.raw_value(event) * event.normalized_intensity()
        if value >= 0.20:
            return 1
        if value <= -0.20:
            return -1
        return 0

    def label(self, reward: int) -> str:
        return {1: "GREEN", 0: "ORANGE", -1: "RED"}[reward]
