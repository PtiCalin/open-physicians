"""Fetch utilities for Australian Health Practitioner Regulation Agency."""

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path("data/raw/oceania/australia/australian_health_practitioner_regulation_agency")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    """Download the latest Australian Health Practitioner Regulation Agency dataset and return the written path."""
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement fetch_latest for ahpra")
