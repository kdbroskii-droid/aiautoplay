from core.events import Event, EventBus
from core.state import AgentState


def test_event_bus_delivers_event() -> None:
    received = []
    bus = EventBus()
    bus.subscribe("test", received.append)
    bus.publish(Event("test", {"value": 1}))
    assert received[0].payload["value"] == 1


def test_agent_state_defaults() -> None:
    state = AgentState()
    assert state.frame == 0
    assert state.last_action == "wait"
