from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrainingMetrics:
    steps: int = 0
    episodes: int = 0
    reward_total: float = 0.0
    good: int = 0
    too_slow: int = 0
    bad: int = 0

    @property
    def average_reward(self) -> float:
        return self.reward_total / self.steps if self.steps else 0.0

    def record(self, reward: int) -> None:
        self.steps += 1
        self.reward_total += reward
        if reward > 0:
            self.good += 1
        elif reward < 0:
            self.bad += 1
        else:
            self.too_slow += 1
