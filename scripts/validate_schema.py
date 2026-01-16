"""Validate cleaned dataset rows against the physician schema."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

SCHEMA_PATH = Path("schemas/physician.schema.json")
DATA_PATH = Path("data/cleaned/physicians_clean.csv")


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    # Placeholder: wire up CSV reading to dict rows before validation
    print(f"Loaded schema with {len(schema.get('properties', {}))} fields")


if __name__ == "__main__":
    main()
