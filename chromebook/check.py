from __future__ import annotations

import os
import platform
import shutil


def main() -> None:
    print("AI AutoPlay Chromebook diagnostics")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"CPU count: {os.cpu_count() or 1}")
    print(f"Available disk: {shutil.disk_usage('.').free / (1024**3):.1f} GiB")


if __name__ == "__main__":
    main()
