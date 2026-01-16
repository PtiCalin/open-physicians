"""Fetch utilities for the CMQ registry."""

from __future__ import annotations

import asyncio
from pathlib import Path

from src.core import http

CMQ_URL = "https://example.org/cmq.csv"
RAW_DIR = Path("data/raw/cmq")


def _target_path() -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    return RAW_DIR / "cmq_latest.csv"


async def fetch_latest() -> Path:
    """Download the latest CMQ dataset asynchronously."""
    response = await http.fetch(CMQ_URL)
    path = _target_path()
    path.write_bytes(response.content)
    return path


def fetch_latest_sync() -> Path:
    """Synchronous convenience wrapper."""
    return asyncio.run(fetch_latest())
