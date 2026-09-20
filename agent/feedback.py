from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class Feedback(IntEnum):
    BAD = -1
    TOO_SLOW = 0
    GOOD = 1


@dataclass(frozen=True)
class FeedbackEvent:
    frame: int
    feedback: Feedback
    reason: str

    @property
    def label(self) -> str:
        return {
            Feedback.GOOD: "GREEN",
            Feedback.TOO_SLOW: "ORANGE",
            Feedback.BAD: "RED",
        }[self.feedback]

    def to_dict(self) -> dict:
        return {
            "frame": self.frame,
            "feedback": int(self.feedback),
            "label": self.label,
            "reason": self.reason,
        }
