from __future__ import annotations

from dataclasses import dataclass, field

from .experience import Experience


@dataclass
class EpisodeMemory:
    """Keeps experiences for one episode and exposes useful summaries."""

    experiences: list[Experience] = field(default_factory=list)

    def add(self, experience: Experience) -> None:
        self.experiences.append(experience)

    @property
    def total_reward(self) -> int:
        return sum(item.reward for item in self.experiences)

    @property
    def length(self) -> int:
        return len(self.experiences)

    def clear(self) -> None:
        self.experiences.clear()
