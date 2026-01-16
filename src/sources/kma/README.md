# Korean Medical Association

- Slug: `kma`
- Region: Asia
- Scope: South Korea
- Raw staging: `data/raw/asia/south_korea/korean_medical_association`

## Purpose
Professional association list, useful as supplemental registry with CAPTCHA hurdles.

## Access Snapshot
Member search portal requiring form POST and occasional CAPTCHA solving.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/asia/south_korea/korean_medical_association`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
