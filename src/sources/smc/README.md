# Singapore Medical Council

- Slug: `smc`
- Region: Asia
- Scope: Singapore
- Raw staging: `data/raw/asia/singapore/singapore_medical_council`

## Purpose
Singapore regulator with searchable register listing register category and conditions.

## Access Snapshot
prs.moh.gov.sg form POST returning HTML tables.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/asia/singapore/singapore_medical_council`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
