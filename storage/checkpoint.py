from __future__ import annotations

from dataclasses import asdict, dataclass
from time import time

from .json_store import JsonStore


@dataclass
class Checkpoint:
    version: int
    created_at: float
    frame: int
    scores: dict[str, float]
    counts: dict[str, int]


class CheckpointStore:
    def __init__(self, store: JsonStore | None = None) -> None:
        self.store = store or JsonStore("data/checkpoints")

    def save(self, frame: int, scores: dict[str, float], counts: dict[str, int]) -> Checkpoint:
        checkpoint = Checkpoint(1, time(), frame, dict(scores), dict(counts))
        self.store.save(f"checkpoint_{frame:08d}.json", asdict(checkpoint))
        self.store.save("latest.json", asdict(checkpoint))
        return checkpoint

    def latest(self) -> Checkpoint | None:
        data = self.store.load("latest.json")
        if not data:
            return None
        return Checkpoint(
            version=int(data["version"]),
            created_at=float(data["created_at"]),
            frame=int(data["frame"]),
            scores={k: float(v) for k, v in data["scores"].items()},
            counts={k: int(v) for k, v in data["counts"].items()},
        )
