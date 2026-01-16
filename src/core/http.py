"""HTTP utilities for authenticated and throttled requests."""

from __future__ import annotations

import httpx


async def fetch(url: str, *, timeout: float = 10.0) -> httpx.Response:
    """Fetch a URL with sane defaults and return the response."""
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response
