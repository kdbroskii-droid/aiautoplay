from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Observation:
    frame: int
    position_x: float
    position_y: float
    visible_target: bool
    standing_still: bool


class ToyEnvironment:
    """Deterministic training environment; it is not connected to any game."""

    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0
        self.frame = 0
        self.last_action = "wait"

    def reset(self) -> Observation:
        self.x = 0.0
        self.y = 0.0
        self.frame = 0
        self.last_action = "wait"
        return self.observe()

    def step(self, action: str) -> Observation:
        self.frame += 1
        self.last_action = action

        if action == "forward":
            self.y += 1.0
        elif action == "backward":
            self.y -= 1.0
        elif action == "left":
            self.x -= 1.0
        elif action == "right":
            self.x += 1.0

        return self.observe()

    def observe(self) -> Observation:
        return Observation(
            frame=self.frame,
            position_x=self.x,
            position_y=self.y,
            visible_target=(self.frame % 20 < 10),
            standing_still=self.last_action == "wait",
        )
