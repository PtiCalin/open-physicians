"""Fetch utilities for Singapore Medical Council."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/asia/singapore/singapore_medical_council")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Singapore Medical Council dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for smc")
