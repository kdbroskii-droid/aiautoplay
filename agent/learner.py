from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    name: str


@dataclass
class LearningStats:
    observations: int = 0
    good: int = 0
    too_slow: int = 0
    bad: int = 0


class RewardLearner:
    """Lightweight sequence-aware learner for the custom sandbox."""

    def __init__(self, history_frames: int = 30) -> None:
        if history_frames < 1:
            raise ValueError("history_frames must be at least 1")
        self.history = deque(maxlen=history_frames)
        self.scores = defaultdict(float)
        self.counts = defaultdict(int)
        self.stats = LearningStats()

    def observe_action(self, action: Action | str) -> None:
        name = action.name if isinstance(action, Action) else action
        self.history.append(name)

    def observe_feedback(self, reward: int) -> None:
        if reward not in (-1, 0, 1):
            raise ValueError("reward must be -1, 0, or 1")

        self.stats.observations += 1
        if reward == 1:
            self.stats.good += 1
        elif reward == 0:
            self.stats.too_slow += 1
        else:
            self.stats.bad += 1

        # Recent actions receive more credit/blame than older actions.
        for distance, name in enumerate(reversed(self.history), start=1):
            weight = 1.0 / distance
            self.scores[name] += reward * weight
            self.counts[name] += 1

    def choose_action(self, actions: list[Action]) -> Action:
        if not actions:
            raise ValueError("actions cannot be empty")
        return max(actions, key=lambda a: (self.scores[a.name], a.name))

    def snapshot(self) -> dict:
        return {
            "scores": dict(self.scores),
            "counts": dict(self.counts),
            "stats": vars(self.stats).copy(),
        }
