# Memory

The memory layer stores what happened during training.

- `Experience` stores state, action, reward, next state, and episode completion.
- `ReplayBuffer` keeps a bounded history for random training samples.
- `EpisodeMemory` tracks one episode and its cumulative reward.

The data structures are local and deterministic when a seed is supplied.
