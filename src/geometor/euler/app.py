"""Command-line interface for ``geometor.euler``."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

__all__ = [
    "build_parser",
    "main",
    "run",
]


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser.

    Returns:
        Configured :class:`argparse.ArgumentParser` instance.
    """
    return argparse.ArgumentParser(
        prog="euler",
        description=(
        "the Swiss mathematician whose 1765 memoir discovered the Euler line "
        "connecting the orthocenter, centroid, and circumcenter of every "
        "triangle"
    ),
    )


def run(argv: Sequence[str] | None = None) -> int:
    """Execute the command-line workflow.

    Args:
        argv: Optional sequence of CLI arguments (defaults to empty list when ``None``).

    Returns:
        Exit code (``0`` on success).
    """
    parser = build_parser()
    parser.parse_args(list(argv) if argv is not None else [])
    return 0


def main() -> None:
    """Console-script entry point."""
    raise SystemExit(run())
