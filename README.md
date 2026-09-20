# AI AutoPlay — Chromebook

A Chromebook/Linux-first 30 FPS AI learning core for a user-owned/custom test environment.

## Core loop
- 30 FPS (~33.3 ms per frame)
- 30-frame action history
- GREEN = +1 — good
- ORANGE = 0 — needs to be quicker
- RED = -1 — bad
- Keyboard/mouse actions represented as an abstract action space
- Frame-by-frame learning logs

## Chromebook

Run from the Linux terminal:

```bash
python3 sandbox/run.py
```

The project is designed to be tested in a sandbox/custom environment. It does not include public-game input injection or anti-cheat bypasses.
