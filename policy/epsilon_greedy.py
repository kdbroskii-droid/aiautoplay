from __future__ import annotations

import random
from collections.abc import Sequence

from agent.learner import Action
from .policy import Policy, PolicyContext


class EpsilonGreedyPolicy(Policy):
    """Balances exploration with learned action scores."""

    def __init__(self, learner, epsilon: float = 0.15, seed: int | None = None) -> None:
        if not 0.0 <= epsilon <= 1.0:
            raise ValueError("epsilon must be between 0 and 1")
        self.learner = learner
        self.epsilon = epsilon
        self.random = random.Random(seed)

    def choose(self, actions: Sequence[Action], context: PolicyContext) -> Action:
        if not actions:
            raise ValueError("actions cannot be empty")
        if self.random.random() < self.epsilon:
            return self.random.choice(list(actions))
        return self.learner.choose_action(list(actions))
