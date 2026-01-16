"""Fetch utilities for BIG Register."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/netherlands/big_register")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest BIG Register dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for big_register")
