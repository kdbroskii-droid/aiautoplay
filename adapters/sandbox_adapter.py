from __future__ import annotations

from observation.interface import ObservationSource
from observation.state import Observation
from sandbox.environment import ToyEnvironment


class SandboxAdapter(ObservationSource):
    """Adapts the deterministic toy environment to the observation interface."""

    def __init__(self, environment: ToyEnvironment | None = None) -> None:
        self.environment = environment or ToyEnvironment()

    def observe(self, frame: int) -> Observation:
        item = self.environment.observe()
        return Observation(
            frame=frame,
            features=(item.position_x, item.position_y, float(item.visible_target), float(item.standing_still)),
            target_visible=item.visible_target,
            danger=1.0 if item.standing_still else 0.0,
        )
