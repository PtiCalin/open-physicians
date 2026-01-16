"""Pipeline transform step."""

from __future__ import annotations

from pathlib import Path
from typing import List

from src.core import dedupe
from src.sources.cmq import parse


def run(raw_path: Path) -> List[dict]:
    """Parse raw files and return deduplicated rows."""
    rows = list(parse.parse_rows(raw_path))
    return dedupe.unique_by_id(rows)
