"""Fetch utilities for Ministerio de Salud Argentina."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/latin_america/argentina/ministerio_de_salud_argentina")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Ministerio de Salud Argentina dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for ministerio_salud_argentina")
