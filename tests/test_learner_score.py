from agent.learner import RewardLearner


def test_score_method_returns_action_score() -> None:
    learner = RewardLearner()
    learner.observe_action("forward")
    learner.observe_feedback(1)
    assert learner.score("forward") > 0
