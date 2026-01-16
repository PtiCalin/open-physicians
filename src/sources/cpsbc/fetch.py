"""Fetch utilities for College of Physicians and Surgeons of British Columbia."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

import httpx

RAW_DIR = Path("data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia")
CPSBC_ENDPOINT = "https://www.cpsbc.ca/physician_directory/search"
DEFAULT_HEADERS = {
    "Accept": "application/json",
    "User-Agent": "open-physicians/0.1 (+https://github.com/PtiCalin/open-physicians)",
    "Referer": "https://www.cpsbc.ca/physician_directory",
}
DEFAULT_PARAMS = {
    "page": 1,
    "pageSize": 100,
    "term": "",
}


def fetch_latest(
    *,
    output_dir: Path | None = None,
    client: httpx.Client | None = None,
    max_pages: int = 1,
    params_factory: Callable[[int], dict[str, Any]] | None = None,
) -> Path:
    """Download the latest CPSBC dataset and return the artifact path."""

    if max_pages < 1:
        raise ValueError("max_pages must be >= 1")

    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    aggregated: list[dict[str, Any]] = []

    def _params_for(page: int) -> dict[str, Any]:
        if params_factory:
            return params_factory(page)
        params = DEFAULT_PARAMS.copy()
        params["page"] = page
        return params

    def _collect_rows(data: dict[str, Any]) -> Iterable[dict[str, Any]]:
        if isinstance(data, dict):
            for key in ("results", "data", "items"):
                rows = data.get(key)
                if isinstance(rows, list):
                    return rows
        if isinstance(data, list):
            return data
        return []

    def _should_continue(data: dict[str, Any], page: int) -> bool:
        if isinstance(data, dict):
            if "hasMore" in data:
                return bool(data["hasMore"])
            if "has_more" in data:
                return bool(data["has_more"])
            if "totalPages" in data:
                return page < int(data["totalPages"])
        return False

    def _run(http_client: httpx.Client) -> None:
        page = 1
        while page <= max_pages:
            params = _params_for(page)
            response = http_client.get(CPSBC_ENDPOINT, params=params, headers=DEFAULT_HEADERS)
            response.raise_for_status()
            data = response.json()
            aggregated.extend(_collect_rows(data))
            if not _should_continue(data, page):
                break
            page += 1

    if client is None:
        with httpx.Client(timeout=30.0) as http_client:
            _run(http_client)
    else:
        _run(client)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = target_dir / f"cpsbc_{timestamp}.json"
    artifact = {
        "source": "cpsbc",
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
        "results": aggregated,
    }
    output_path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output_path
