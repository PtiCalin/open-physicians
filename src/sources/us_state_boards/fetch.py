"""Fetch utilities for United States State Medical Boards."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/north_america/united_states/state_medical_boards")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest United States State Medical Boards dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for us_state_boards")
