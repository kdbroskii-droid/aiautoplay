from __future__ import annotations

from agent.actions import InputAction
from .controller import PhysicalController


KEYS = {"W", "A", "S", "D", "SPACE", "SHIFT", "E", "R"}


class ActionDispatcher:
    """Translate abstract AI actions into local-controller operations."""

    def __init__(self, controller: PhysicalController) -> None:
        self.controller = controller

    def dispatch(self, action: InputAction) -> None:
        if action.name in {"forward", "backward", "left", "right", "jump", "sprint", "interact", "reload"}:
            key = str(action.value)
            if key not in KEYS:
                raise ValueError(f"unsupported key: {key}")
            self.controller.press(key)
            return

        if action.name == "mouse_move":
            value = action.value or {}
            self.controller.mouse_move(int(value.get("dx", 0)), int(value.get("dy", 0)))
            return

        if action.name in {"mouse_left", "mouse_right"}:
            button = "left" if action.name == "mouse_left" else "right"
            self.controller.mouse_button(button, True)
            return

        if action.name == "wait":
            return

        raise ValueError(f"unsupported action: {action.name}")
