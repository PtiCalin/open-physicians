"""Fetch utilities for Direccion General de Profesiones."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/north_america/mexico/direccion_general_de_profesiones")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Direccion General de Profesiones dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for dgp_mexico")
