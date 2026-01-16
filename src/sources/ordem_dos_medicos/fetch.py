"""Fetch utilities for Ordem dos Medicos."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/portugal/ordem_dos_medicos")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Ordem dos Medicos dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for ordem_dos_medicos")
