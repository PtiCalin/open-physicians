"""Fetch utilities for Royal College of Physicians and Surgeons of Canada."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/north_america/canada/royal_college_of_physicians_and_surgeons_of_canada")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Royal College of Physicians and Surgeons of Canada dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for rcpsc")
