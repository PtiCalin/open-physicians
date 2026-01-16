# Data Sources

This repository prioritizes authoritative medical regulators with open or semi-open registers. Each entry below should map directly to a `data/raw/...` directory and include live scrape notes, licensing terms, and refresh cadence in its README.

## North America

| Entity | Scope | Notes |
| --- | --- | --- |
| College des medecins du Quebec (CMQ) | Quebec, CA | CSV downloads via public register; canonical CMQ feed already wired to `src/sources/cmq`. |
| College of Physicians and Surgeons of Ontario (CPSO) | Ontario, CA | JSON search endpoint (`GetDoctors`); track CPSO number and profile URL. |
| College of Physicians and Surgeons of British Columbia (CPSBC) | British Columbia, CA | JSON API behind form search; include status history snapshots. |
| College of Physicians and Surgeons of Alberta (CPSA) | Alberta, CA | AJAX search with ASP.NET session; capture practice location coordinates. |
| Royal College of Physicians and Surgeons of Canada | Canada (certification) | Join table for specialty validation—do not treat as licensing authority. |
| Federation of State Medical Boards (FSMB) | United States index | Directory of state boards; drive scheduling for per-state scrapers. |
| Individual State Medical Boards | United States | Create subdirectories per state; respect board-specific terms, CAPTCHA, or FOIA requirements. |
| Direccion General de Profesiones | Mexico | National license lookup with reCAPTCHA; store cedula-professional mappings. |

## Europe

| Entity | Scope | Notes |
| --- | --- | --- |
| General Medical Council (GMC) | United Kingdom | JSON API with sanctions history; map GMC reference to canonical ID. |
| Irish Medical Council (IMC) | Ireland | AJAX endpoint requires anti-forgery token; capture division, specialty, status. |
| Conseil National de l'Ordre des Medecins (CNOM) | France | GraphQL API delivering RPPS IDs, addresses, and specialty info. |
| Bundesarztekammer | Germany | Aggregator for Landesaerztekammern; spawn downstream jobs per state chamber. |
| BIG Register | Netherlands | REST API with pagination; capture BIG number and validity dates. |
| Organizacion Medica Colegial (CGCOM) | Spain | Provincial colleges with heterogeneous formats; consolidate province codes. |
| Federazione Nazionale degli Ordini dei Medici (FNOMCeO) | Italy | JSON API with nonce; retain provincial order metadata. |
| Ordem dos Medicos | Portugal | Form-based search; translate specialty labels before normalization. |
| Ordre des Medecins | Belgium | Bilingual HTML listings; capture both FR/NL fields. |
| MedReg | Switzerland | REST API supporting anonymous access; respect `X-RateLimit` headers. |
| Socialstyrelsen | Sweden | JSON search; include Swedish titles alongside normalized values. |
| Valvira | Finland | CSV exports triggered per query; preserve bilingual metadata. |
| Danish Patient Safety Authority | Denmark | OData JSON with API keys; capture authorization types. |
| Norwegian Directorate of Health | Norway | Daily CSV dump (`hpr-full`); store checksums for integrity. |

## Oceania

| Entity | Scope | Notes |
| --- | --- | --- |
| Australian Health Practitioner Regulation Agency (AHPRA) | Australia | JSON practitioner search; include conditions and undertakings. |
| Medical Council of New Zealand (MCNZ) | New Zealand | JSON endpoint with scopes of practice and registration status. |

## Asia

| Entity | Scope | Notes |
| --- | --- | --- |
| Ministry of Health, Labour and Welfare (MHLW) | Japan | Aggregated statistics; convert PDF tables to CSV for macro indicators. |
| Korean Medical Association (KMA) | South Korea | Association member lookup; partial coverage with CAPTCHA. |
| National Medical Commission (NMC) | India | REST endpoint with CAPTCHA; track state council origin. |
| Singapore Medical Council (SMC) | Singapore | HTML/JSON hybrid; capture register category and conditions. |
| Medical Council of Hong Kong (MCHK) | Hong Kong | XLS register downloads; parse bilingual notes. |

## Middle East

| Entity | Scope | Notes |
| --- | --- | --- |
| Ministry of Health Israel | Israel | SPA with REST API; store Hebrew and English transliterations. |
| Dubai Health Authority (DHA) | UAE (Dubai) | ASP.NET service with strict throttles; capture facility affiliation. |
| Department of Health Abu Dhabi (DOH) | UAE (Abu Dhabi) | Public API with optional key; dedupe with DHA dataset. |

## Africa

| Entity | Scope | Notes |
| --- | --- | --- |
| Health Professions Council of South Africa (HPCSA) | South Africa | reCAPTCHA-protected lookup; prefer FOI exports for bulk data. |
| Medical and Dental Council of Nigeria (MDCN) | Nigeria | API with CAPTCHA; document consent requirements. |
| Kenya Medical Practitioners and Dentists Council (KMPDC) | Kenya | PDF registers per profession; automate PDF→CSV pipeline. |

## Latin America

| Entity | Scope | Notes |
| --- | --- | --- |
| Conselho Federal de Medicina (CFM) | Brazil | AJAX search returning CRM and specialty info; respect LGPD. |
| Ministerio de Salud Argentina (REFEPS) | Argentina | SOAP/REST hybrid requiring API key; capture province codes. |
| Superintendencia de Salud | Chile | XLS downloads; convert to UTF-8 CSV and log version numbers. |

## International Meta Sources

| Entity | Scope | Notes |
| --- | --- | --- |
| World Health Organization (WHO) | Global | Global Health Observatory API for workforce density indicators. |
| OECD | OECD members | SDMX datasets for physicians per capita and specialty mixes. |
| World Directory of Medical Schools (WDOMS) | Global | GraphQL API; join table for training origin metadata. |

## Specialty / Supplemental Registries

Use specialty colleges (e.g., Royal College surgical subspecialties, psychiatry boards, family medicine colleges, anesthesiology societies) once the core national register coverage is stable. Track their provenance in `data/raw/specialty/...` and document their compatibility with the canonical schema.

## Expansion Guidance

- Mirror every new source in both `docs/sources.md` and its matching `data/raw` README.
- Record access URLs, rate limits, authentication, and legal policies before running scrapers.
- Keep `data/metadata/scrape_log.csv` updated with completed pulls, schema changes, and blockers.
