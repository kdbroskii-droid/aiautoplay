from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    name: str


class RewardLearner:
    """Small tabular learner for a sandbox environment."""

    def __init__(self, history_frames: int = 30) -> None:
        self.history = deque(maxlen=history_frames)
        self.scores = defaultdict(float)

    def observe_action(self, action: Action) -> None:
        self.history.append(action.name)

    def observe_feedback(self, reward: int) -> None:
        if reward not in (-1, 0, 1):
            raise ValueError("reward must be -1, 0, or 1")

        # Give the most recent actions the strongest credit/blame.
        recent = list(self.history)
        for distance, name in enumerate(reversed(recent), start=1):
            weight = 1.0 / distance
            self.scores[name] += reward * weight

    def choose_action(self, actions: list[Action]) -> Action:
        if not actions:
            raise ValueError("actions cannot be empty")

        # Deterministic tie-breaking keeps the simulator reproducible.
        return max(actions, key=lambda a: (self.scores[a.name], a.name))

    def snapshot(self) -> dict[str, float]:
        return dict(self.scores)
