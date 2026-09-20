from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence

from agent.learner import Action


@dataclass(frozen=True)
class PolicyContext:
    frame: int
    danger: float = 0.0
    target_visible: bool = False


class Policy(ABC):
    @abstractmethod
    def choose(self, actions: Sequence[Action], context: PolicyContext) -> Action:
        raise NotImplementedError
