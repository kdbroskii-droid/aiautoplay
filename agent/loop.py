from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Frame:
    number: int
    timestamp: float


class FrameLoop:
    """30 FPS loop with drift-resistant scheduling."""

    def __init__(self, fps: float = 30.0) -> None:
        if fps <= 0:
            raise ValueError("fps must be positive")
        self.fps = fps
        self.period = 1.0 / fps

    def run(
        self,
        callback: Callable[[Frame], None],
        frames: int | None = None,
    ) -> None:
        started = time.perf_counter()
        frame_number = 0

        while frames is None or frame_number < frames:
            target = started + frame_number * self.period
            now = time.perf_counter()
            if now < target:
                time.sleep(target - now)

            frame = Frame(frame_number, time.time())
            callback(frame)
            frame_number += 1
