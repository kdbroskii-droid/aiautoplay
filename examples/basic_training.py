from __future__ import annotations

from agent.learner import Action
from training.trainer import Trainer


def main() -> None:
    actions = [Action(name) for name in ("forward", "backward", "left", "right", "wait")]
    trainer = Trainer(actions)
    state = (0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    for frame in range(30):
        action = trainer.choose(state, frame)
        reward = 1 if action.name == "forward" else 0
        trainer.record(frame, state, action, reward, state)
    print("steps:", trainer.metrics.steps)
    print("average reward:", trainer.metrics.average_reward)
    print("scores:", trainer.learner.snapshot()["scores"])


if __name__ == "__main__":
    main()
