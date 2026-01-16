# Norwegian Directorate of Health

- Slug: `norwegian_directorate_of_health`
- Region: Europe
- Scope: Norway
- Raw staging: `data/raw/europe/nordic/norwegian_directorate_of_health`

## Purpose
Norwegian HPR dataset distributed as daily CSV exports.

## Access Snapshot
Download hpr-full dataset from data.helsedirektoratet.no.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/nordic/norwegian_directorate_of_health`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
