# Architecture

## Runtime loop

1. Observation arrives.
2. The agent chooses an abstract action.
3. The sandbox executes that action.
4. The sandbox produces an observation.
5. Feedback is converted to -1, 0, or +1.
6. The learner updates its action scores.
7. The next 30 FPS frame begins.

## Timing

The target period is 1/30 second, approximately 33.333 ms.

The frame loop uses a monotonic clock for scheduling so processing time does not permanently shift later frames.

## Safety boundary

The repository is structured around a user-owned/custom sandbox. It does not implement public-game input injection, anti-cheat bypasses, or live-match automation.
