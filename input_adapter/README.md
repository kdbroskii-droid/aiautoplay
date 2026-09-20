# Physical input adapter

This is the boundary between the AI's abstract actions and a physical-input implementation.

It is intentionally disabled by default and contains no OS-level key injection. For a game you own, connect `PhysicalController` to that game's local test/input bridge.

The AI can therefore produce actions such as `forward`, `jump`, and `mouse_move` without coupling the learning system to a particular operating system.
