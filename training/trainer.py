from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

from agent.learner import Action, RewardLearner
from memory.experience import Experience
from memory.replay_buffer import ReplayBuffer
from policy.epsilon_greedy import EpsilonGreedyPolicy
from policy.policy import PolicyContext
from .metrics import TrainingMetrics


@dataclass(frozen=True)
class TrainingConfig:
    replay_capacity: int = 10_000
    batch_size: int = 32
    epsilon: float = 0.15
    seed: int | None = 0


class Trainer:
    """Connects observation, policy, reward, and replay memory."""

    def __init__(self, actions: Sequence[Action], config: TrainingConfig | None = None) -> None:
        self.config = config or TrainingConfig()
        self.actions = list(actions)
        self.learner = RewardLearner(history_frames=30)
        self.policy = EpsilonGreedyPolicy(self.learner, self.config.epsilon, self.config.seed)
        self.replay = ReplayBuffer(self.config.replay_capacity, self.config.seed)
        self.metrics = TrainingMetrics()

    def choose(self, state: tuple[float, ...], frame: int, danger: float = 0.0, target_visible: bool = False) -> Action:
        return self.policy.choose(
            self.actions,
            PolicyContext(frame=frame, danger=danger, target_visible=target_visible),
        )

    def record(self, frame: int, state: tuple[float, ...], action: Action, reward: int, next_state: tuple[float, ...], done: bool = False) -> None:
        if reward not in (-1, 0, 1):
            raise ValueError("reward must be -1, 0, or 1")
        self.learner.observe_action(action)
        self.learner.observe_feedback(reward)
        self.replay.add(Experience(frame, state, action.name, reward, next_state, done))
        self.metrics.record(reward)
        if done:
            self.metrics.episodes += 1

    def sample_batch(self) -> list[Experience]:
        return self.replay.sample(self.config.batch_size)
