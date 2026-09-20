from agent.actions import Device, InputAction
from input_adapter.controller import PhysicalController
from input_adapter.dispatcher import ActionDispatcher


def test_dispatcher_rejects_disabled_controller() -> None:
    dispatcher = ActionDispatcher(PhysicalController(enabled=False))
    try:
        dispatcher.dispatch(InputAction("forward", Device.KEYBOARD, "W"))
    except RuntimeError:
        return
    raise AssertionError("disabled physical input was accepted")
