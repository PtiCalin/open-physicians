# Ordre des Medecins (Belgium)

- Slug: `ordre_des_medecins`
- Region: Europe
- Scope: Belgium
- Raw staging: `data/raw/europe/belgium/ordre_des_medecins`

## Purpose
Belgian order publishing bilingual listings requiring pagination crawls.

## Access Snapshot
HTML listings at ordomedic.be with filter parameters.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/belgium/ordre_des_medecins`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
