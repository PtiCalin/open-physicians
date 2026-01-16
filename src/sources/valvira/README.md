# Valvira

- Slug: `valvira`
- Region: Europe
- Scope: Finland
- Raw staging: `data/raw/europe/nordic/valvira`

## Purpose
Finnish supervisory authority with CSV exports for healthcare professionals.

## Access Snapshot
Downloadable CSV triggered by query parameters on valvira.fi.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/nordic/valvira`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
