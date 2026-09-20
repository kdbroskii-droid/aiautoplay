from agent.learner import Action, RewardLearner


def test_reward_updates_score() -> None:
    learner = RewardLearner()
    learner.observe_action(Action("forward"))
    learner.observe_feedback(1)
    assert learner.score("forward") > 0


def test_invalid_reward_rejected() -> None:
    learner = RewardLearner()
    learner.observe_action("forward")
    try:
        learner.observe_feedback(2)
    except ValueError:
        return
    raise AssertionError("invalid reward was accepted")
