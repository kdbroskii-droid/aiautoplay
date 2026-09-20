from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI AutoPlay Chromebook tools")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("info", help="show basic runtime information")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "info":
        from chromebook.check import main as check_main
        check_main()
    else:
        build_parser().print_help()


if __name__ == "__main__":
    main()
