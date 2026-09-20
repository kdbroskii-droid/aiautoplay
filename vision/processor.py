from __future__ import annotations

from .features import FeatureVector
from .frame import FrameObservation


class ObservationProcessor:
    """Convert a frame observation into stable numeric features.

    This is deliberately backend-agnostic: a custom environment can provide
    pixels or already-computed metadata without requiring OS input hooks.
    """

    def process(self, frame: FrameObservation) -> FeatureVector:
        if frame.width < 0 or frame.height < 0:
            raise ValueError("frame dimensions cannot be negative")

        # Pixel decoding is intentionally left to an environment-specific
        # adapter. An empty frame still produces a valid neutral observation.
        return FeatureVector()
