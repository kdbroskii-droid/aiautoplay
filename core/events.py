from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    name: str
    payload: dict[str, object]


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, name: str, handler: Callable[[Event], None]) -> None:
        self._handlers[name].append(handler)

    def publish(self, event: Event) -> None:
        for handler in tuple(self._handlers.get(event.name, ())):
            handler(event)
