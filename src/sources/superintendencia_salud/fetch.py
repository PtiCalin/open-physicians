"""Fetch utilities for Superintendencia de Salud."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/latin_america/chile/superintendencia_de_salud")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Superintendencia de Salud dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for superintendencia_salud")
