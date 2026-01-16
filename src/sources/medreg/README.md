# MedReg

- Slug: `medreg`
- Region: Europe
- Scope: Switzerland
- Raw staging: `data/raw/europe/switzerland/medreg`

## Purpose
Swiss federal register with REST API returning multilingual JSON payloads.

## Access Snapshot
api/Medreg/v1/persons with optional API key.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/switzerland/medreg`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
