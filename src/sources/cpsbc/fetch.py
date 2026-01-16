"""Fetch utilities for College of Physicians and Surgeons of British Columbia."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest College of Physicians and Surgeons of British Columbia dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for cpsbc")
