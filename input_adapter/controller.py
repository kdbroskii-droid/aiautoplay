from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PhysicalController:
    """Physical-input boundary for a user-owned/local test application."""

    enabled: bool = True

    def press(self, key: str) -> None:
        self._require_enabled()
        raise NotImplementedError("Connect press() to your own test application's input bridge")

    def release(self, key: str) -> None:
        self._require_enabled()
        raise NotImplementedError("Connect release() to your own test application's input bridge")

    def mouse_move(self, dx: int, dy: int) -> None:
        self._require_enabled()
        raise NotImplementedError("Connect mouse_move() to your own test application's input bridge")

    def mouse_button(self, button: str, pressed: bool) -> None:
        self._require_enabled()
        raise NotImplementedError("Connect mouse_button() to your own test application's input bridge")

    def _require_enabled(self) -> None:
        if not self.enabled:
            raise RuntimeError("Physical input is disabled")
