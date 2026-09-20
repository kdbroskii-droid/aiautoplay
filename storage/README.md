# Storage

The storage layer keeps the AI's learned state on the Chromebook.

- `JsonStore` provides simple atomic JSON files.
- `CheckpointStore` saves timestamped checkpoints plus `latest.json`.

Runtime data is kept under `data/`, which should not be committed to Git.
