"""Source adapter for Medical and Dental Council of Nigeria."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
