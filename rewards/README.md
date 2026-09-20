# Rewards

The reward layer translates events into the project's three training labels:

- GREEN = `+1`
- ORANGE = `0`
- RED = `-1`

Supported event categories include movement, shooting, weapon classification,
building, editing, eliminations, pickups, interactions, objectives, standing
still, circular movement, missed actions, and death.

Weights are configurable through `RewardWeights` so a custom sandbox can tune
what it considers useful behavior.
