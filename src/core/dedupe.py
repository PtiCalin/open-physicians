"""Record deduplication helpers."""

from __future__ import annotations

from typing import Iterable, List


def unique_by_id(rows: Iterable[dict]) -> List[dict]:
    """Return rows keeping the first occurrence of each physician_id."""
    seen = set()
    output: List[dict] = []
    for row in rows:
        physician_id = row.get("physician_id")
        if physician_id in seen:
            continue
        seen.add(physician_id)
        output.append(row)
    return output
