"""Fetch utilities for Kenya Medical Practitioners and Dentists Council."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/africa/kenya/kenya_medical_practitioners_and_dentists_council")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Kenya Medical Practitioners and Dentists Council dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for kmpdc")
