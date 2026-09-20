from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationResult:
    reward: int
    label: str
    reason: str


def evaluate_reward(reward: int, reason: str = "") -> EvaluationResult:
    if reward not in (-1, 0, 1):
        raise ValueError("reward must be -1, 0, or 1")
    label = {1: "GREEN", 0: "ORANGE", -1: "RED"}[reward]
    return EvaluationResult(reward, label, reason)
