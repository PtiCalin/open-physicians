# Open Physicians

Open Physicians curates a public, replicable pipeline for collecting and standardizing global physician registries. This repository hosts documentation, schemas, ingestion code, and datasets used to build a transparent open-data release.

## Repository Layout

- `docs/` high-level methodology, ethics, and data dictionary
- `src/` reusable ingestion and transformation modules
- `data/` raw inputs, cleaned exports, and supporting metadata
- `scripts/` runnable utilities for scraping, validation, and exports
- `.github/` issue templates and automation

## Getting Started

1. Create and activate a Python 3.11+ virtual environment
2. Install dependencies with `pip install -r requirements.txt`
3. Review `docs/overview.md` for data sourcing context
4. Run `scripts/run_scraper.py` to fetch the CMQ source

Contributions are welcome. Please open an issue with proposed enhancements or questions before submitting a pull request.
