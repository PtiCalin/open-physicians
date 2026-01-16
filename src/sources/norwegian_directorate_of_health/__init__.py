"""Source adapter for Norwegian Directorate of Health."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
