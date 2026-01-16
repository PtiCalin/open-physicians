"""Fetch utilities for National Medical Commission."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/asia/india/national_medical_commission")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest National Medical Commission dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for nmc")
