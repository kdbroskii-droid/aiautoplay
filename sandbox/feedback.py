from __future__ import annotations

from agent.feedback import Feedback
from agent.actions import InputAction
from .environment import Observation


def evaluate(observation: Observation, action: InputAction) -> tuple[Feedback, str]:
    """Produce simple training feedback for the toy environment."""
    if observation.standing_still:
        return Feedback.BAD, "standing still"

    if action.name == "forward" and observation.visible_target:
        return Feedback.GOOD, "moving while a target is visible"

    if action.name in {"left", "right"}:
        return Feedback.TOO_SLOW, "movement is useful but needs better timing"

    return Feedback.TOO_SLOW, "action needs better timing"
