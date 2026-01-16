"""Fetch utilities for Ordre des Medecins (Belgium)."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/belgium/ordre_des_medecins")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Ordre des Medecins (Belgium) dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for ordre_des_medecins")
