"""Source adapter for College of Physicians and Surgeons of Alberta."""

from .fetch import fetch_latest
from .parse import iter_records

__all__ = ["fetch_latest", "iter_records"]
