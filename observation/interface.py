from __future__ import annotations

from abc import ABC, abstractmethod

from .state import Observation


class ObservationSource(ABC):
    @abstractmethod
    def observe(self, frame: int) -> Observation:
        raise NotImplementedError
