from __future__ import annotations

from agent.actions import DEFAULT_ACTIONS
from agent.feedback import Feedback
from agent.learner import Action, RewardLearner
from agent.loop import Frame, FrameLoop
from .environment import ToyEnvironment
from .feedback import evaluate


def main() -> None:
    env = ToyEnvironment()
    learner = RewardLearner(history_frames=30)
    actions = [Action(a.name) for a in DEFAULT_ACTIONS if a.name in {
        "forward", "backward", "left", "right", "jump", "wait"
    }]

    env.reset()
    print("AI AutoPlay sandbox — 30 FPS")
    print("Chromebook/Linux mode. No external input injection.")

    def tick(frame: Frame) -> None:
        action = learner.choose_action(actions)
        learner.observe_action(action)

        observation = env.step(action.name)
        feedback, reason = evaluate(observation, next(
            a for a in DEFAULT_ACTIONS if a.name == action.name
        ))
        learner.observe_feedback(int(feedback))

        print(
            f"frame={frame.number:04d} "
            f"action={action.name:<8} "
            f"feedback={feedback.name:<9} "
            f"reward={int(feedback):+d} "
            f"reason={reason}"
        )

    FrameLoop(30).run(tick, frames=300)

    print("\nLearned scores:")
    for name, score in sorted(learner.scores.items()):
        print(f"  {name:<10} {score:+.3f}")


if __name__ == "__main__":
    main()
