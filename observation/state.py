from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Observation:
    frame: int
    features: tuple[float, ...] = field(default_factory=tuple)
    target_visible: bool = False
    danger: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.danger <= 1.0:
            raise ValueError("danger must be between 0 and 1")
