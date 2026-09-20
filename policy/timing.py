from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ActionTiming:
    cooldown_frames: int = 0
    last_frame: int = -10**9

    def ready(self, frame: int) -> bool:
        return frame - self.last_frame >= self.cooldown_frames

    def mark(self, frame: int) -> None:
        self.last_frame = frame
