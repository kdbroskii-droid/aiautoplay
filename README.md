# AI AutoPlay — Chromebook

A Chromebook/Linux-first 30 FPS AI learning core for a user-owned/custom test environment.

## Run

```bash
./run.sh
```

Diagnostics:

```bash
python3 -m cli.main info
```

Validation:

```bash
python3 -m tools.validate
```

Tests:

```bash
python3 -m pytest -q
```

The runtime uses Python's standard library. The repository includes action handling, feedback, history, learning, sandboxing, vision, observations, policies, memory, training, rewards, storage, logging, core events, Chromebook diagnostics, evaluation, adapters, UI, profiling, benchmarks, examples, tests, and GitHub CI.

## Safety boundary

This repository is intended for a user-owned/custom sandbox or simulator. It does not implement public-game input injection, anti-cheat bypasses, or live-match automation.
