"""Pipeline extract step."""

from __future__ import annotations

from pathlib import Path

from src.sources.cmq import fetch


def run() -> Path:
    """Trigger all extract jobs and return the latest artifact path."""
    return fetch.fetch_latest_sync()
