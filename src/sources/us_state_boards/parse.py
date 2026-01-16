"""Parsing helpers for United States State Medical Boards."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterator


def iter_records(raw_path: Path) -> Iterator[Dict[str, str]]:
    """Yield canonicalized records extracted from the raw artifact."""
    raise NotImplementedError("Implement iter_records for us_state_boards")
