# Bundesarztekammer

- Slug: `bundesaerztekammer`
- Region: Europe
- Scope: Germany
- Raw staging: `data/raw/europe/germany/bundesaerztekammer`

## Purpose
German federal body listing state chambers; orchestrates downstream scrapes.

## Access Snapshot
Static HTML linking to each Landesaerztekammer portal.

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `data/raw/europe/germany/bundesaerztekammer`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
