"""Fetch utilities for Federazione Nazionale degli Ordini dei Medici."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/europe/italy/federazione_nazionale_degli_ordini_dei_medici")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Federazione Nazionale degli Ordini dei Medici dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for fnomceo")
