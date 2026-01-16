# Kenya Medical Practitioners and Dentists Council

- Slug: `kmpdc`
- Region: Africa
- Scope: Kenya
- Raw staging: `data/raw/africa/kenya/kenya_medical_practitioners_and_dentists_council`

## Purpose
Kenyan council publishing PDF registers per profession.

## Access Snapshot
Download PDF registers and convert to CSV.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/africa/kenya/kenya_medical_practitioners_and_dentists_council`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
