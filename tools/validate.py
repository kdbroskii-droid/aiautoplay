from __future__ import annotations

import importlib


MODULES = ("agent", "sandbox", "vision", "policy", "memory", "training", "rewards", "storage", "core", "observation", "evaluation")


def main() -> int:
    failed = []
    for name in MODULES:
        try:
            importlib.import_module(name)
            print(f"OK   {name}")
        except Exception as exc:
            failed.append((name, exc))
            print(f"FAIL {name}: {exc}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
