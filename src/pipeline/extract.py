"""Pipeline extract step."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict

from src.sources.cmq import fetch as cmq_fetch
from src.sources.cpsbc import fetch as cpsbc_fetch
from src.sources.cpso import fetch as cpso_fetch

SCRAPE_LOG_PATH = Path("data/metadata/scrape_log.csv")

SourceFetcher = Callable[[], Path]

SOURCE_FETCHERS: Dict[str, SourceFetcher] = {
    "cmq": cmq_fetch.fetch_latest_sync,
    "cpso": cpso_fetch.fetch_latest,
    "cpsbc": cpsbc_fetch.fetch_latest,
}


def _append_scrape_log(rows: list[tuple[str, str, str, str]]) -> None:
    SCRAPE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = SCRAPE_LOG_PATH.exists()
    with SCRAPE_LOG_PATH.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if not file_exists:
            writer.writerow(["timestamp", "source", "status", "details"])
        writer.writerows(rows)


def run(
    *,
    fetch_overrides: Dict[str, SourceFetcher] | None = None,
    log_scrapes: bool = True,
) -> Dict[str, Path]:
    """Trigger all extract jobs and return artifacts keyed by source slug."""

    artifacts: Dict[str, Path] = {}
    log_rows: list[tuple[str, str, str, str]] = []

    for slug, fetcher in SOURCE_FETCHERS.items():
        fetch_impl = fetcher
        if fetch_overrides and slug in fetch_overrides:
            fetch_impl = fetch_overrides[slug]
        timestamp = datetime.now(timezone.utc).isoformat()
        try:
            artifact_path = fetch_impl()
        except Exception as exc:  # pragma: no cover - propagated but logged
            log_rows.append((timestamp, slug, "error", str(exc)))
            if log_scrapes:
                _append_scrape_log(log_rows)
            raise
        artifacts[slug] = artifact_path
        log_rows.append((timestamp, slug, "success", str(artifact_path)))

    if log_scrapes and log_rows:
        _append_scrape_log(log_rows)

    return artifacts
