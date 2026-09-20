# Architecture

AI AutoPlay is split into independent layers:

- `vision/` describes frame observations.
- `observation/` defines environment-facing observation contracts.
- `policy/` chooses abstract actions.
- `agent/` stores action history and reward learning.
- `memory/` stores experiences.
- `rewards/` converts events into -1/0/+1 feedback.
- `training/` connects policy, learning, and replay memory.
- `storage/` persists checkpoints locally.
- `core/` provides shared state and events.
- `telemetry`/`logging` records runtime information.
- `adapters/` connects custom environments to the common interfaces.
- `ui/` and `cli/` expose lightweight local tools.

The architecture deliberately keeps environment adapters separate from public-game automation or anti-cheat bypass mechanisms.
