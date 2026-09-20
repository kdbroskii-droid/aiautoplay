import pytest

from observation.state import Observation


def test_observation_accepts_normal_danger() -> None:
    item = Observation(frame=1, danger=0.5)
    assert item.danger == 0.5


def test_observation_rejects_invalid_danger() -> None:
    with pytest.raises(ValueError):
        Observation(frame=1, danger=2.0)
