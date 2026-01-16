"""Parsing helpers for College of Physicians and Surgeons of Ontario."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterator, Sequence

from src.core.normalize import normalize_name

PROVINCE_TO_ISO = {
    "ON": "CA-ON",
}


def _load_rows(raw_path: Path) -> Sequence[dict]:
    payload = json.loads(raw_path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        for key in ("results", "Results", "data"):
            rows = payload.get(key)
            if isinstance(rows, list):
                return rows
    if isinstance(payload, list):
        return payload
    return []


def _normalize_name(row: dict) -> str:
    candidate = row.get("fullName") or row.get("name")
    if not candidate:
        first = row.get("firstName") or row.get("first_name")
        last = row.get("lastName") or row.get("last_name")
        candidate = " ".join(part for part in (first, last) if part)
    return normalize_name(candidate or "")


def _province_code(row: dict) -> str:
    province = None
    location = row.get("practiceLocation") or {}
    if isinstance(location, dict):
        province = location.get("province") or location.get("state")
    province = province or row.get("province") or row.get("practiceProvince")
    if not province:
        return PROVINCE_TO_ISO["ON"]
    province_norm = str(province).strip().upper()
    return PROVINCE_TO_ISO.get(province_norm, province_norm)


def iter_records(raw_path: Path) -> Iterator[Dict[str, str]]:
    """Yield canonicalized records extracted from the raw artifact."""

    for row in _load_rows(raw_path):
        registration_number = row.get("registrationNumber") or row.get("registration_number")
        if not registration_number:
            continue
        registration_str = str(registration_number).strip()
        if not registration_str:
            continue
        yield {
            "physician_id": f"cpso-{registration_str}",
            "full_name": _normalize_name(row),
            "license_status": row.get("registrationStatus") or row.get("status"),
            "specialty_code": row.get("primarySpecialty") or row.get("specialty"),
            "location_code": _province_code(row),
            "source": "cpso",
            "updated_at": row.get("lastUpdated") or row.get("last_updated"),
        }
