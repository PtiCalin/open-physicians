"""Source adapter for BIG Register."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
