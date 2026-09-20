from __future__ import annotations

from time import perf_counter

from agent.loop import FrameLoop


def main() -> None:
    count = 300
    started = perf_counter()
    FrameLoop(30).run(lambda frame: None, frames=count)
    elapsed = perf_counter() - started
    print(f"frames={count} elapsed={elapsed:.3f}s")
    print(f"effective_fps={count / elapsed:.2f}")


if __name__ == "__main__":
    main()
