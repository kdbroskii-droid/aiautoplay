from agent.actions import Device, InputAction
from agent.feedback import Feedback
from sandbox.environment import Observation
from sandbox.feedback import evaluate


def test_standing_still_is_bad() -> None:
    observation = Observation(1, 0, 0, False, True)
    action = InputAction("wait", Device.KEYBOARD)
    feedback, _ = evaluate(observation, action)
    assert feedback == Feedback.BAD
