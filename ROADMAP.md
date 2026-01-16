# Open Physicians Roadmap

This roadmap scopes the strategic pathway for standing up a trustworthy, refreshable physician licensing database. Timelines assume a lean team with part-time contributors; adjust as resourcing evolves.

## Guiding Principles

1. **Verifiable sourcing** — every record must link to an auditable regulator artifact.
2. **Incremental delivery** — release usable slices of the dataset as each geography stabilizes.
3. **Compliance-first** — respect legal, ethical, and technical constraints for each registry.
4. **Automation with manual fallbacks** — script when possible but document FOI/manual paths when required.

## Phase Overview

| Phase | Duration | Goal | Key Deliverables |
| --- | --- | --- | --- |
| Phase 0: Foundation | Weeks 0-2 | Solid scaffolding and governance | Repo scaffold (done), docs, CI, release log, roadmap |
| Phase 1: Source Readiness | Weeks 2-6 | Production-ready Tier 1 regulators | Completed source READMEs, access credentials, scrape proof-of-concepts, updated `scrape_log.csv` |
| Phase 2: Pipeline Alpha | Weeks 6-10 | End-to-end CMQ+CPSO pipeline | Automated extract/transform/load jobs, schema validation harness, first `data/cleaned` snapshot |
| Phase 3: Canada Coverage | Weeks 10-16 | Nationwide Canadian dataset | CPSBC/CPSA ingestion, Royal College joins, coverage dashboards |
| Phase 4: US Pilot | Weeks 16-24 | Representative US state sample | FSMB-driven job scheduler, 3 large states (CA/NY/TX) with compliance notes |
| Phase 5: European Expansion | Weeks 24-32 | GMC, IMC, CNOM, BIG integrated | Locale-aware normalization, multilingual QA scripts |
| Phase 6: Global Enrichment | Weeks 32+ | Meta-data joins + specialty registries | WHO/OECD indicators, WDOMS linking, specialty board overlays |

## Detailed Milestones

### Phase 1 — Source Readiness
- Finalize access method, throttle, and legal notes in each `data/raw/.../README.md` (script-supported).
- Populate `data/metadata/scrape_log.csv` with planned cadence per source.
- Secure credentials or approvals for restricted endpoints (e.g., FOI, API keys).
- Add backlog issues per source covering engineering tasks, compliance checks, and data QA.

### Phase 2 — Pipeline Alpha
- Promote `src/sources/cmq` to production quality (retry logic, checksum logging).
- Implement `src/sources/cpso` module mirroring CMQ structure.
- Flesh out `src/pipeline/transform.py` with mapping lookups and schema validation hooks.
- Add pytest suite covering normalization, dedupe, and schema compliance.
- Automate CI job to run `scripts/run_scraper.py` in dry-run mode for regression detection.

### Phase 3 — Canada Coverage
- Build CPSBC and CPSA fetchers with throttling + CSV persistence.
- Integrate Royal College certification data as a lookup table (non-authoritative for licensing).
- Produce Canada-wide `physicians_clean.csv` plus coverage metrics (counts per province/status/specialty).
- Publish methodology update in `docs/methodology.md` and release note entry for v0.2.0.

### Phase 4 — United States Pilot
- Derive job manifest from FSMB directory and store in `data/metadata/`.
- Implement per-state plugins starting with California, New York, Texas (handle CAPTCHA/paywalls).
- Introduce job scheduler (Airflow, Prefect, or lightweight cron orchestrator) for state-specific cadence.
- Design escalation process for manual/FOI workflows when automation blocked.

### Phase 5 — Europe Expansion
- Localize normalization utilities for multilingual name, specialty, and address handling.
- Add GraphQL/REST clients for GMC, IMC, CNOM, BIG with rate-limit aware batching.
- Build translation glossary for specialty labels and legal statuses.
- Run cross-country QA comparing WHO/OECD aggregates with aggregated license counts.

### Phase 6 — Global Enrichment
- Wire WHO/OECD/WDOMS datasets into a `data/reference/` folder with versioned metadata.
- Develop enrichment jobs that join macro indicators and education provenance to physician records.
- Onboard specialty-specific registries (e.g., psychiatry, surgery) and align to canonical schema.
- Publish transparency dashboard summarizing coverage, refresh cadence, and known gaps.

## Cross-Cutting Workstreams

- **Compliance & Ethics:** maintain removal policy, legal reviews, and audit trails per source.
- **Quality Assurance:** implement automated validation (schema, duplicate detection) plus manual spot checks.
- **Observability:** log scrape stats, failures, and latency in a lightweight dashboard or notebook.
- **Community Contributions:** tag issues per source complexity, document onboarding steps, and encourage data donations.

## Release Cadence

- Target quarterly tagged releases (`v0.x.0`) capturing new geographies or major features.
- Publish delta notes in `data/metadata/release_notes.md` and summarize in the README.
- Between releases, share `data/cleaned/previews/` snapshots for early adopters to test integration.

## Risks & Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Access revoked due to scraping | High | Engage regulators early, provide value statements, offer to share cleaned outputs. |
| CAPTCHA / anti-bot escalation | Medium | Invest in hybrid automation (human-in-loop), respect rate limits, explore official data-sharing agreements. |
| Schema drift between sources | Medium | Version schema, add automated diff detection, enforce contract tests. |
| Team bandwidth limits | Medium | Prioritize Tier 1 regulators, document onboarding for contributors, scope stretch goals separately. |

## Next Actions

1. File backlog issues for each Phase 1 source detailing engineering tasks and compliance owners.
2. Stand up credential vault or secure storage for API keys and FOI exports.
3. Schedule a roadmap review after Phase 2 to reassess sequencing and resource needs.
