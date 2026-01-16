"""Source adapter for Department of Health Abu Dhabi."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
