"""Core application logic for Codex Testnet."""

from __future__ import annotations


def normalize_name(name: str) -> str:
    """Normalize user-provided names for greetings."""
    stripped = name.strip()
    return stripped if stripped else "friend"


def greet(name: str) -> str:
    """Return a friendly greeting."""
    safe_name = normalize_name(name)
    return f"Hello, {safe_name}!"
