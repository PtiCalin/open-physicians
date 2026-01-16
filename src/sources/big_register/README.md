# BIG Register

- Slug: `big_register`
- Region: Europe
- Scope: Netherlands
- Raw staging: `data/raw/europe/netherlands/big_register`

## Purpose
Dutch national register with REST API delivering BIG numbers and validity dates.

## Access Snapshot
/api/Registrations with pagination tokens and Accept-Language header.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/netherlands/big_register`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
