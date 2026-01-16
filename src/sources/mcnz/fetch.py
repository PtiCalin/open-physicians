"""Fetch utilities for Medical Council of New Zealand."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/oceania/new_zealand/medical_council_of_new_zealand")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Medical Council of New Zealand dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for mcnz")
