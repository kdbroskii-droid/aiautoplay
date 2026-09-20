from __future__ import annotations

from collections import deque
from math import hypot


class MovementDetector:
    """Detects prolonged stillness and simple circular movement patterns."""

    def __init__(self, history: int = 30) -> None:
        self.positions = deque(maxlen=history)

    def update(self, x: float, y: float) -> tuple[bool, bool]:
        self.positions.append((x, y))
        if len(self.positions) < 4:
            return False, False

        points = list(self.positions)
        movement = sum(hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(points, points[1:]))
        still = movement < 0.01

        # A lightweight heuristic: lots of movement with little net displacement.
        net = hypot(points[-1][0] - points[0][0], points[-1][1] - points[0][1])
        circular = movement > 3.0 and net < movement * 0.20
        return still, circular
