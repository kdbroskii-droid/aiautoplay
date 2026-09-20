from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Device(str, Enum):
    KEYBOARD = "keyboard"
    MOUSE = "mouse"


@dataclass(frozen=True)
class InputAction:
    name: str
    device: Device
    value: object | None = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "device": self.device.value,
            "value": self.value,
        }


DEFAULT_ACTIONS = (
    InputAction("forward", Device.KEYBOARD, "W"),
    InputAction("backward", Device.KEYBOARD, "S"),
    InputAction("left", Device.KEYBOARD, "A"),
    InputAction("right", Device.KEYBOARD, "D"),
    InputAction("jump", Device.KEYBOARD, "SPACE"),
    InputAction("sprint", Device.KEYBOARD, "SHIFT"),
    InputAction("interact", Device.KEYBOARD, "E"),
    InputAction("reload", Device.KEYBOARD, "R"),
    InputAction("mouse_left", Device.MOUSE, "LEFT"),
    InputAction("mouse_right", Device.MOUSE, "RIGHT"),
    InputAction("mouse_move", Device.MOUSE, {"dx": 0, "dy": 0}),
    InputAction("wait", Device.KEYBOARD, None),
)
