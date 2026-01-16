"""Fetch utilities for Dubai Health Authority."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/middle_east/united_arab_emirates/dubai_health_authority")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Dubai Health Authority dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for dha")
