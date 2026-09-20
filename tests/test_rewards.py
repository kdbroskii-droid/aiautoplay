from rewards.events import RewardEvent, RewardEventType
from rewards.shaping import RewardShaper


def test_positive_event_is_green() -> None:
    result = RewardShaper().reward(RewardEvent(RewardEventType.MOVE, 1))
    assert result == 1


def test_death_is_red() -> None:
    result = RewardShaper().reward(RewardEvent(RewardEventType.DEATH, 1))
    assert result == -1
