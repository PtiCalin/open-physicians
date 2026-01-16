# Release Notes

## v0.1.0 - Initial Scaffold
- Adds repository structure and placeholder datasets
- Documents methodology, ethics, and source overview
- Adds tiered registry roadmap covering core sources and expansion guidance
- Adds placeholder directories and notes for global regulator and meta-data sources
- Details scrape URLs, throttle guidance, and legal references per source README
- Adds scripts/maintenance/update_source_placeholders.py to regenerate docs programmatically
- Adds scripts/maintenance/scaffold_source_modules.py plus initial adapter scaffolding and registry docs
- Documents adapter structure/status in src/sources/README.md and seeds packages for every regulator listed in docs/sources.md
- Implements CPSO and CPSBC adapters (fetch/parse/mapping) with regression tests under tests/sources/
- Updates pipeline extract/transform to orchestrate CMQ+CPSO+CPSBC and append scrape runs to data/metadata/scrape_log.csv
- Adds scripts/dev/run_stub_extract.py to exercise the pipeline locally and seed the first real scrape log entries
