# Methodology

1. **Ingest** raw registries using `src/sources/*/fetch.py`
2. **Parse** to structured rows using tuned parsers per source
3. **Normalize** identifiers, specialties, and geographies using shared core utilities
4. **Validate** against JSON Schema and mapping tables
5. **Publish** cleaned CSV exports and accompanying metadata
