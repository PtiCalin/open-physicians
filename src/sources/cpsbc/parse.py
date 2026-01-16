"""Parsing helpers for College of Physicians and Surgeons of British Columbia."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterator, Sequence

from src.core.normalize import normalize_name

PROVINCE_CODE = "CA-BC"


def _load_rows(raw_path: Path) -> Sequence[dict]:
    payload = json.loads(raw_path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        for key in ("results", "data", "items"):
            rows = payload.get(key)
            if isinstance(rows, list):
                return rows
    if isinstance(payload, list):
        return payload
    return []


def _name_from_row(row: dict) -> str:
    if row.get("fullName"):
        return normalize_name(str(row["fullName"]))
    parts = [row.get("firstName") or row.get("first_name"), row.get("lastName") or row.get("last_name")]
    joined = " ".join(part for part in parts if part)
    return normalize_name(joined)


def _location_code(row: dict) -> str:
    province = row.get("practiceProvince") or row.get("province")
    if not province:
        return PROVINCE_CODE
    normalized = str(province).strip().upper()
    if normalized in {"BC", "B.C.", "BRITISH COLUMBIA", PROVINCE_CODE}:
        return PROVINCE_CODE
    return normalized


def iter_records(raw_path: Path) -> Iterator[Dict[str, str]]:
    """Yield canonicalized records extracted from the raw artifact."""

    for row in _load_rows(raw_path):
        identifier = row.get("cpid") or row.get("registrationId") or row.get("id")
        if not identifier:
            continue
        identifier_str = str(identifier).strip()
        if not identifier_str:
            continue
        yield {
            "physician_id": f"cpsbc-{identifier_str}",
            "full_name": _name_from_row(row),
            "license_status": row.get("registration_status") or row.get("status"),
            "specialty_code": row.get("specialty") or row.get("primarySpecialty"),
            "location_code": _location_code(row),
            "source": "cpsbc",
            "updated_at": row.get("last_modified") or row.get("updatedAt"),
        }
