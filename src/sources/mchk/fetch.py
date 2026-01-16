"""Fetch utilities for Medical Council of Hong Kong."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/asia/hong_kong/medical_council_of_hong_kong")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Medical Council of Hong Kong dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for mchk")
