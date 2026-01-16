"""Fetch utilities for World Health Organization."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/international/meta/world_health_organization")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest World Health Organization dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for who")
