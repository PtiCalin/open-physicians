"""Fetch utilities for Conseil National de l'Ordre des Medecins."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/france/conseil_national_de_l_ordre_des_medecins")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Conseil National de l'Ordre des Medecins dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for cnom")
