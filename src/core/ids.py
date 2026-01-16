"""Identifier helpers."""

from __future__ import annotations

import ulid


def new_physician_id() -> str:
    """Return a sortable ULID string for a physician."""
    return str(ulid.ULID())
