"""Common normalization utilities."""

from __future__ import annotations

import unicodedata


def normalize_name(value: str) -> str:
    """Normalize unicode, collapse whitespace, and title-case names."""
    cleaned = unicodedata.normalize("NFKC", value).strip()
    parts = [segment for segment in cleaned.split() if segment]
    return " ".join(part.capitalize() for part in parts)
