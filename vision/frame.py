from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FrameObservation:
    """Compact, serializable description of one observed frame."""

    frame: int
    timestamp: float
    width: int
    height: int
    pixels: bytes = field(repr=False, default=b"")

    def has_pixels(self) -> bool:
        return bool(self.pixels)
