from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureVector:
    """Numerical features supplied to the policy/learner."""

    motion_x: float = 0.0
    motion_y: float = 0.0
    target_visible: float = 0.0
    target_distance: float = 1.0
    danger: float = 0.0
    interaction_available: float = 0.0

    def as_tuple(self) -> tuple[float, ...]:
        return (
            self.motion_x,
            self.motion_y,
            self.target_visible,
            self.target_distance,
            self.danger,
            self.interaction_available,
        )
