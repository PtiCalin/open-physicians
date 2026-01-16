"""Pipeline load step."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

OUTPUT_PATH = Path("data/cleaned/physicians_clean.csv")


def run(rows: Iterable[dict]) -> Path:
    """Write cleaned rows to the default CSV output."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        raise ValueError("No rows provided to load step")

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    return OUTPUT_PATH
