"""Source adapter for Federazione Nazionale degli Ordini dei Medici."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
