from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonStore:
    """Small atomic JSON persistence helper for local Chromebook storage."""

    def __init__(self, root: str | Path = "data") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, name: str, value: Any) -> Path:
        path = self.root / name
        if path.suffix != ".json":
            path = path.with_suffix(".json")
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
        temporary.replace(path)
        return path

    def load(self, name: str, default: Any = None) -> Any:
        path = self.root / name
        if path.suffix != ".json":
            path = path.with_suffix(".json")
        if not path.exists():
            return default
        return json.loads(path.read_text(encoding="utf-8"))
