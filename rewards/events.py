from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RewardEventType(str, Enum):
    MOVE = "move"
    SHOOT = "shoot"
    CLASSIFY = "classify"
    BUILD = "build"
    EDIT = "edit"
    ELIMINATION = "elimination"
    PICKUP = "pickup"
    INTERACT = "interact"
    TARGET_ACQUIRED = "target_acquired"
    OBJECTIVE_PROGRESS = "objective_progress"
    STANDING_STILL = "standing_still"
    CIRCULAR_MOVEMENT = "circular_movement"
    DEATH = "death"
    MISSED_ACTION = "missed_action"


@dataclass(frozen=True)
class RewardEvent:
    event_type: RewardEventType
    frame: int
    intensity: float = 1.0
    detail: str = ""

    def normalized_intensity(self) -> float:
        return max(0.0, min(1.0, self.intensity))
