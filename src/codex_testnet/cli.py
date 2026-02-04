"""Command-line interface for Codex Testnet."""

from __future__ import annotations

import argparse

from codex_testnet.app import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Codex Testnet CLI")
    parser.add_argument("name", nargs="?", default="", help="Name to greet")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    message = greet(args.name)
    print(message)


if __name__ == "__main__":
    main()
