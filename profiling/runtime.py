from __future__ import annotations

from contextlib import contextmanager
from time import perf_counter
from collections.abc import Iterator


@contextmanager
def measure(name: str) -> Iterator[None]:
    started = perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (perf_counter() - started) * 1000.0
        print(f"[profile] {name}: {elapsed_ms:.3f} ms")
