from __future__ import annotations

from collections.abc import Iterable

from agent.learner import Action
from .policy import PolicyContext


def filter_actions(actions: Iterable[Action], context: PolicyContext) -> list[Action]:
    result = list(actions)
    if context.danger > 0.9:
        result = [a for a in result if a.name != "wait"]
    return result or list(actions)
