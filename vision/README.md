# Vision

The vision layer turns observations from a user-owned/custom environment into
compact numerical features.

The core API is intentionally backend-agnostic. Later adapters can provide
screen images, simulator frames, or synthetic observations without coupling
the learner to a particular game or operating-system input system.

No public-game automation or anti-cheat integration belongs in this folder.
