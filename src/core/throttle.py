"""Async-friendly throttling helpers."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator


@asynccontextmanager
async def rate_limit(delay_seconds: float) -> AsyncIterator[None]:
    """Serialize tasks by sleeping for the configured delay."""
    try:
        yield
    finally:
        await asyncio.sleep(delay_seconds)
