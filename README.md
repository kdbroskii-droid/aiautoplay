# AI AutoPlay — Chromebook

A Chromebook/Linux-first 30 FPS AI learning core for a user-owned/custom test environment.

## Repository structure

- `agent/` — action, feedback, timing, history, and learning core
- `sandbox/` — deterministic toy environment and runner
- `tests/` — automated checks
- `config/` — project configuration documentation
- `docs/` — architecture and design notes
- `logs/` — runtime logs (ignored by Git)
- `run.sh` — Chromebook/Linux launcher

## Core loop

30 FPS → observe → choose abstract action → sandbox step → feedback → learn → repeat.

Feedback:
- GREEN = +1 — good
- ORANGE = 0 — needs to be quicker
- RED = -1 — bad

## Chromebook

Open the Linux terminal in ChromeOS and run:

```bash
cd ~/aiautoplay
python3 sandbox/run.py
```

Or:

```bash
./run.sh
```

## Tests

If pytest is installed:

```bash
python3 -m pytest
```

The project uses the Python standard library for its runtime.

## Safety boundary

This repository is intended for a user-owned/custom sandbox or simulator. It does not implement public-game input injection, anti-cheat bypasses, or live-match automation.
