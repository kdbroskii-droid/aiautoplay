from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class HistoryEntry:
    frame: int
    action: str
    feedback: int | None = None


class ActionHistory:
    def __init__(self, max_frames: int = 30) -> None:
        if max_frames < 1:
            raise ValueError("max_frames must be at least 1")
        self.entries = deque(maxlen=max_frames)

    def add(self, frame: int, action: str, feedback: int | None = None) -> None:
        self.entries.append(HistoryEntry(frame, action, feedback))

    def recent(self) -> list[HistoryEntry]:
        return list(self.entries)
