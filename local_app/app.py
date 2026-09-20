from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass

from agent.learner import Action, RewardLearner


@dataclass
class Player:
    x: int = 220
    y: int = 180
    speed: int = 8


class LocalTestApp:
    """A small user-owned/local window used to test AI decisions safely."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("AI AutoPlay — Local Test")
        self.root.geometry("640x420")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=640, height=360, highlightthickness=0)
        self.canvas.pack()
        self.status = tk.Label(self.root, text="AI local test — no external input")
        self.status.pack(fill="x")

        self.player = Player()
        self.target = (520, 180)
        self.learner = RewardLearner(history_frames=30)
        self.actions = [Action(x) for x in ("forward", "backward", "left", "right", "wait")]
        self.frame = 0
        self.running = True

        self.root.bind("<Escape>", lambda _event: self.stop())
        self.draw()
        self.root.after(33, self.tick)

    def draw(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 640, 360, outline="")
        self.canvas.create_oval(
            self.target[0] - 14, self.target[1] - 14,
            self.target[0] + 14, self.target[1] + 14,
            outline="green", width=3
        )
        self.canvas.create_rectangle(
            self.player.x - 12, self.player.y - 12,
            self.player.x + 12, self.player.y + 12,
            outline="blue", width=3
        )
        self.canvas.create_text(
            10, 10, anchor="nw",
            text=f"frame {self.frame} | GREEN +1 / ORANGE 0 / RED -1"
        )

    def step(self, name: str) -> int:
        old = (self.player.x, self.player.y)
        if name == "forward":
            self.player.y -= self.player.speed
        elif name == "backward":
            self.player.y += self.player.speed
        elif name == "left":
            self.player.x -= self.player.speed
        elif name == "right":
            self.player.x += self.player.speed

        self.player.x = max(15, min(625, self.player.x))
        self.player.y = max(15, min(345, self.player.y))

        distance = abs(self.player.x - self.target[0]) + abs(self.player.y - self.target[1])
        moved = (self.player.x, self.player.y) != old
        if distance < 30:
            return 1
        if not moved:
            return -1
        return 0

    def tick(self) -> None:
        if not self.running:
            return
        self.frame += 1
        action = self.learner.choose_action(self.actions)
        self.learner.observe_action(action)
        reward = self.step(action.name)
        self.learner.observe_feedback(reward)
        label = {1: "GREEN", 0: "ORANGE", -1: "RED"}[reward]
        self.status.config(text=f"AI action: {action.name} | {label} ({reward:+d}) | Esc = stop")
        self.draw()
        self.root.after(33, self.tick)

    def stop(self) -> None:
        self.running = False
        self.root.destroy()


def main() -> None:
    LocalTestApp().root.mainloop()


if __name__ == "__main__":
    main()
