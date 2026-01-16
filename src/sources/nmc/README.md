# National Medical Commission

- Slug: `nmc`
- Region: Asia
- Scope: India
- Raw staging: `data/raw/asia/india/national_medical_commission`

## Purpose
Indian national register accessible via REST endpoint returning JSON records.

## Access Snapshot
MCIRest verifyDetails endpoint plus CAPTCHA token per session.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/asia/india/national_medical_commission`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
