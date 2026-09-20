from agent.learner import Action, RewardLearner
from policy.epsilon_greedy import EpsilonGreedyPolicy
from policy.policy import PolicyContext


def test_policy_is_deterministic_with_zero_epsilon() -> None:
    learner = RewardLearner()
    learner.observe_action("forward")
    learner.observe_feedback(1)
    policy = EpsilonGreedyPolicy(learner, epsilon=0.0, seed=1)
    result = policy.choose([Action("wait"), Action("forward")], PolicyContext(frame=1))
    assert result.name == "forward"
