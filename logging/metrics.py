from __future__ import annotations

import csv
from pathlib import Path


class MetricsLogger:
    def __init__(self, path: str | Path = "logs/metrics.csv") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, row: dict[str, object]) -> None:
        exists = self.path.exists()
        with self.path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(row))
            if not exists:
                writer.writeheader()
            writer.writerow(row)
