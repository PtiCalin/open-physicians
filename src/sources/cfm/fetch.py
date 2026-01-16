"""Fetch utilities for Conselho Federal de Medicina."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/latin_america/brazil/conselho_federal_de_medicina")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Conselho Federal de Medicina dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for cfm")
