"""Fetch utilities for Medical and Dental Council of Nigeria."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/africa/nigeria/medical_and_dental_council_of_nigeria")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Medical and Dental Council of Nigeria dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for mdcn")
