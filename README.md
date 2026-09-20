# AI AutoPlay — Safe Sandbox Learning Core

A 30 FPS reinforcement-learning prototype for a user-owned/custom sandbox.

## What it does
- Samples one observation every 33.3 ms.
- Records the last 30 actions.
- Uses three feedback values:
  - green = +1 (good)
  - orange = 0 (needs to be quicker)
  - red = -1 (bad)
- Learns action/feedback associations without injecting input into public games.
- Includes a simple simulator so the learning loop can be tested before connecting any game.

## Run

```bash
python3 sandbox/run.py
```

This project intentionally does not include public-game input injection, anti-cheat bypasses, or automation for live matches.
