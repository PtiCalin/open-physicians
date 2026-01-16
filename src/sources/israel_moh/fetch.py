"""Fetch utilities for Ministry of Health Israel."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/middle_east/israel/ministry_of_health_israel")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Ministry of Health Israel dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for israel_moh")
