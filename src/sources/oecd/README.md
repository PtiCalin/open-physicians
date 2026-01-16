# OECD

- Slug: `oecd`
- Region: International
- Scope: OECD members
- Raw staging: `data/raw/international/meta/oecd`

## Purpose
OECD SDMX datasets for physician per capita metrics.

## Access Snapshot
stats.oecd.org SDMX-JSON queries.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/international/meta/oecd`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
