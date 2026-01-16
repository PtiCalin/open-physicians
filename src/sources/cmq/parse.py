"""Parsing helpers for CMQ CSV exports."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterator

from src.core import normalize


def parse_rows(path: Path) -> Iterator[Dict[str, str]]:
    """Yield normalized row dicts from the CMQ CSV file."""
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield {
                "physician_id": row.get("Numero"),
                "full_name": normalize.normalize_name(row.get("Nom", "")),
                "specialty_code": row.get("Specialite"),
                "license_status": row.get("Statut"),
                "location_code": row.get("Region"),
                "source": "cmq",
            }
