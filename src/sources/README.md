# Source Adapters

Each subpackage under `src/sources/` encapsulates the fetching and parsing logic for a single regulator, registry, or supplemental dataset described in [docs/sources.md](../../docs/sources.md). Modules follow a consistent structure so they can plug into the shared pipeline with minimal friction.

## Module Layout

Every adapter directory contains:

- `README.md` — overview, data scope, access notes, and implementation checklist
- `fetch.py` — network client that downloads raw artifacts into the associated `data/raw/...` directory (use async or sync patterns as appropriate)
- `parse.py` — transforms raw payloads into canonical dictionaries ready for normalization
- `mapping.yaml` — documents source→canonical field mappings and codebooks
- `__init__.py` — exports `fetch_latest` and `iter_records` for pipeline consumption

Use `scripts/maintenance/scaffold_source_modules.py` whenever a new regulator needs onboarding. The script creates the baseline directory structure, placeholder files, and boilerplate documentation; engineers then fill in the real logic, tests, and metadata.

## Module Registry

Status legend: `alpha` = wired into the pipeline; `todo` = scaffolding exists, implementation pending.

### North America

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `cmq` | College des medecins du Quebec | Quebec, Canada | `data/raw/north_america/canada/college_des_medecins_du_quebec` | alpha |
| `cpso` | College of Physicians and Surgeons of Ontario | Ontario, Canada | `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_ontario` | todo |
| `cpsbc` | College of Physicians and Surgeons of British Columbia | British Columbia, Canada | `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia` | todo |
| `cpsa` | College of Physicians and Surgeons of Alberta | Alberta, Canada | `data/raw/north_america/canada/college_of_physicians_and_surgeons_of_alberta` | todo |
| `rcpsc` | Royal College of Physicians and Surgeons of Canada | Canada (certification) | `data/raw/north_america/canada/royal_college_of_physicians_and_surgeons_of_canada` | todo |
| `fsmb` | Federation of State Medical Boards | United States (index) | `data/raw/north_america/united_states/federation_of_state_medical_boards` | todo |
| `us_state_boards` | United States State Medical Boards | United States | `data/raw/north_america/united_states/state_medical_boards` | todo |
| `dgp_mexico` | Direccion General de Profesiones | Mexico | `data/raw/north_america/mexico/direccion_general_de_profesiones` | todo |

### Europe

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `gmc` | General Medical Council | United Kingdom | `data/raw/europe/united_kingdom_and_ireland/general_medical_council` | todo |
| `imc` | Irish Medical Council | Ireland | `data/raw/europe/united_kingdom_and_ireland/irish_medical_council` | todo |
| `cnom` | Conseil National de l'Ordre des Medecins | France | `data/raw/europe/france/conseil_national_de_l_ordre_des_medecins` | todo |
| `bundesaerztekammer` | Bundesarztekammer | Germany | `data/raw/europe/germany/bundesaerztekammer` | todo |
| `big_register` | BIG Register | Netherlands | `data/raw/europe/netherlands/big_register` | todo |
| `cgcom` | Organizacion Medica Colegial | Spain | `data/raw/europe/spain/organizacion_medica_colegial` | todo |
| `fnomceo` | Federazione Nazionale degli Ordini dei Medici | Italy | `data/raw/europe/italy/federazione_nazionale_degli_ordini_dei_medici` | todo |
| `ordem_dos_medicos` | Ordem dos Medicos | Portugal | `data/raw/europe/portugal/ordem_dos_medicos` | todo |
| `ordre_des_medecins` | Ordre des Medecins (Belgium) | Belgium | `data/raw/europe/belgium/ordre_des_medecins` | todo |
| `medreg` | MedReg | Switzerland | `data/raw/europe/switzerland/medreg` | todo |
| `socialstyrelsen` | Socialstyrelsen | Sweden | `data/raw/europe/nordic/socialstyrelsen` | todo |
| `valvira` | Valvira | Finland | `data/raw/europe/nordic/valvira` | todo |
| `danish_patient_safety_authority` | Danish Patient Safety Authority | Denmark | `data/raw/europe/nordic/danish_patient_safety_authority` | todo |
| `norwegian_directorate_of_health` | Norwegian Directorate of Health | Norway | `data/raw/europe/nordic/norwegian_directorate_of_health` | todo |

### Oceania

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `ahpra` | Australian Health Practitioner Regulation Agency | Australia | `data/raw/oceania/australia/australian_health_practitioner_regulation_agency` | todo |
| `mcnz` | Medical Council of New Zealand | New Zealand | `data/raw/oceania/new_zealand/medical_council_of_new_zealand` | todo |

### Asia

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `mhlw` | Ministry of Health Labour and Welfare | Japan | `data/raw/asia/japan/ministry_of_health_labour_and_welfare` | todo |
| `kma` | Korean Medical Association | South Korea | `data/raw/asia/south_korea/korean_medical_association` | todo |
| `nmc` | National Medical Commission | India | `data/raw/asia/india/national_medical_commission` | todo |
| `smc` | Singapore Medical Council | Singapore | `data/raw/asia/singapore/singapore_medical_council` | todo |
| `mchk` | Medical Council of Hong Kong | Hong Kong | `data/raw/asia/hong_kong/medical_council_of_hong_kong` | todo |

### Middle East

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `israel_moh` | Ministry of Health Israel | Israel | `data/raw/middle_east/israel/ministry_of_health_israel` | todo |
| `dha` | Dubai Health Authority | United Arab Emirates (Dubai) | `data/raw/middle_east/united_arab_emirates/dubai_health_authority` | todo |
| `doh_abu_dhabi` | Department of Health Abu Dhabi | United Arab Emirates (Abu Dhabi) | `data/raw/middle_east/united_arab_emirates/department_of_health_abu_dhabi` | todo |

### Africa

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `hpcsa` | Health Professions Council of South Africa | South Africa | `data/raw/africa/south_africa/health_professions_council_of_south_africa` | todo |
| `mdcn` | Medical and Dental Council of Nigeria | Nigeria | `data/raw/africa/nigeria/medical_and_dental_council_of_nigeria` | todo |
| `kmpdc` | Kenya Medical Practitioners and Dentists Council | Kenya | `data/raw/africa/kenya/kenya_medical_practitioners_and_dentists_council` | todo |

### Latin America

| Slug | Regulator | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `cfm` | Conselho Federal de Medicina | Brazil | `data/raw/latin_america/brazil/conselho_federal_de_medicina` | todo |
| `ministerio_salud_argentina` | Ministerio de Salud Argentina | Argentina | `data/raw/latin_america/argentina/ministerio_de_salud_argentina` | todo |
| `superintendencia_salud` | Superintendencia de Salud | Chile | `data/raw/latin_america/chile/superintendencia_de_salud` | todo |

### International / Meta

| Slug | Dataset | Scope | Raw staging | Status |
| --- | --- | --- | --- | --- |
| `who` | World Health Organization | Global | `data/raw/international/meta/world_health_organization` | todo |
| `oecd` | OECD | OECD members | `data/raw/international/meta/oecd` | todo |
| `wdoms` | World Directory of Medical Schools | Global | `data/raw/international/meta/world_directory_of_medical_schools` | todo |