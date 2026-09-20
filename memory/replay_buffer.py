from __future__ import annotations

import random
from collections import deque

from .experience import Experience


class ReplayBuffer:
    """Bounded experience memory with reproducible random sampling."""

    def __init__(self, capacity: int = 10_000, seed: int | None = None) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self.data = deque(maxlen=capacity)
        self.random = random.Random(seed)

    def add(self, experience: Experience) -> None:
        self.data.append(experience)

    def sample(self, size: int) -> list[Experience]:
        if size < 1:
            raise ValueError("size must be at least 1")
        return self.random.sample(list(self.data), min(size, len(self.data)))

    def __len__(self) -> int:
        return len(self.data)
