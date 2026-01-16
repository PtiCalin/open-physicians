"""Pipeline transform step."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Dict, Iterable, List, Mapping

from src.core import dedupe
from src.sources.cmq import parse as cmq_parse
from src.sources.cpsbc import parse as cpsbc_parse
from src.sources.cpso import parse as cpso_parse

Parser = Callable[[Path], Iterable[dict]]

SOURCE_PARSERS: Dict[str, Parser] = {
    "cmq": cmq_parse.parse_rows,
    "cpso": cpso_parse.iter_records,
    "cpsbc": cpsbc_parse.iter_records,
}


def run(raw_artifacts: Mapping[str, Path]) -> List[dict]:
    """Parse raw files from multiple sources and return deduplicated rows."""

    combined_rows: List[dict] = []
    for slug, raw_path in raw_artifacts.items():
        parser = SOURCE_PARSERS.get(slug)
        if parser is None:
            raise KeyError(f"No parser registered for source '{slug}'")
        parsed_rows = list(parser(raw_path))
        combined_rows.extend(parsed_rows)
    return dedupe.unique_by_id(combined_rows)
