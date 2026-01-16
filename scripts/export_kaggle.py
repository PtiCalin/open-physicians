"""Placeholder script to package cleaned data for Kaggle uploads."""

from __future__ import annotations

from pathlib import Path

DATA_PATH = Path("data/cleaned/physicians_clean.csv")


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError("Run scripts/run_scraper.py before exporting")
    print(f"Ready to package {DATA_PATH}")


if __name__ == "__main__":
    main()
