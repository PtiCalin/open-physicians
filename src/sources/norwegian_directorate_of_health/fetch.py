"""Fetch utilities for Norwegian Directorate of Health."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/nordic/norwegian_directorate_of_health")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Norwegian Directorate of Health dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for norwegian_directorate_of_health")
