"""Source adapter for Medical Council of Hong Kong."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
