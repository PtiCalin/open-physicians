"""Scaffold source adapter packages under src/sources."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCES_DIR = REPO_ROOT / "src" / "sources"

SOURCES = [
    {
        "slug": "cmq",
        "name": "College des medecins du Quebec",
        "region": "North America",
        "scope": "Quebec, Canada",
        "raw_path": "data/raw/north_america/canada/college_des_medecins_du_quebec",
        "description": "Primary Quebec regulator used for initial pipeline bring-up.",
        "access": "Public CSV download after acknowledging legal notice; mirrors RAW_DIR.",
        "status": "alpha",
    },
    {
        "slug": "cpso",
        "name": "College of Physicians and Surgeons of Ontario",
        "region": "North America",
        "scope": "Ontario, Canada",
        "raw_path": "data/raw/north_america/canada/college_of_physicians_and_surgeons_of_ontario",
        "description": "Ontario regulator with JSON search endpoint providing CPSO numbers and status.",
        "access": "POST to GetDoctors JSON endpoint; anti-bot headers required.",
        "status": "todo",
    },
    {
        "slug": "cpsbc",
        "name": "College of Physicians and Surgeons of British Columbia",
        "region": "North America",
        "scope": "British Columbia, Canada",
        "raw_path": "data/raw/north_america/canada/college_of_physicians_and_surgeons_of_british_columbia",
        "description": "BC regulator with JSON-backed directory containing status history.",
        "access": "Form POST hitting /physician_directory/search returning JSON pages.",
        "status": "todo",
    },
    {
        "slug": "cpsa",
        "name": "College of Physicians and Surgeons of Alberta",
        "region": "North America",
        "scope": "Alberta, Canada",
        "raw_path": "data/raw/north_america/canada/college_of_physicians_and_surgeons_of_alberta",
        "description": "Alberta regulator exposing AJAX lookup results with practice locations.",
        "access": "AJAX calls to /PhysicianSearch/Lookup requiring ASP.NET session.",
        "status": "todo",
    },
    {
        "slug": "rcpsc",
        "name": "Royal College of Physicians and Surgeons of Canada",
        "region": "North America",
        "scope": "Canada (certification)",
        "raw_path": "data/raw/north_america/canada/royal_college_of_physicians_and_surgeons_of_canada",
        "description": "Certification directory used as specialty join table rather than licensing authority.",
        "access": "HTML form returning tables; parse via BeautifulSoup or lxml.",
        "status": "todo",
    },
    {
        "slug": "fsmb",
        "name": "Federation of State Medical Boards",
        "region": "North America",
        "scope": "United States (index)",
        "raw_path": "data/raw/north_america/united_states/federation_of_state_medical_boards",
        "description": "National index of US state boards powering downstream per-state jobs.",
        "access": "Static HTML directory; scrape board metadata and contact info.",
        "status": "todo",
    },
    {
        "slug": "us_state_boards",
        "name": "United States State Medical Boards",
        "region": "North America",
        "scope": "United States",
        "raw_path": "data/raw/north_america/united_states/state_medical_boards",
        "description": "Container for state-specific adapters (California, New York, Texas, etc.).",
        "access": "Varies per board: CSV, HTML, PDF, SOAP, or portal logins.",
        "status": "todo",
    },
    {
        "slug": "dgp_mexico",
        "name": "Direccion General de Profesiones",
        "region": "North America",
        "scope": "Mexico",
        "raw_path": "data/raw/north_america/mexico/direccion_general_de_profesiones",
        "description": "Mexican federal license lookup for cedula-professional mapping.",
        "access": "cedulaprof portal with reCAPTCHA-protected JSON responses.",
        "status": "todo",
    },
    {
        "slug": "gmc",
        "name": "General Medical Council",
        "region": "Europe",
        "scope": "United Kingdom",
        "raw_path": "data/raw/europe/united_kingdom_and_ireland/general_medical_council",
        "description": "UK regulator with JSON API including sanctions and status history.",
        "access": "REST endpoint /api/gmc/Registrations supporting pagination.",
        "status": "todo",
    },
    {
        "slug": "imc",
        "name": "Irish Medical Council",
        "region": "Europe",
        "scope": "Ireland",
        "raw_path": "data/raw/europe/united_kingdom_and_ireland/irish_medical_council",
        "description": "Irish regulator returning JSON rows with registration division and specialty.",
        "access": "AJAX posts to /RegisterSearch/api/Doctors with anti-forgery token.",
        "status": "todo",
    },
    {
        "slug": "cnom",
        "name": "Conseil National de l'Ordre des Medecins",
        "region": "Europe",
        "scope": "France",
        "raw_path": "data/raw/europe/france/conseil_national_de_l_ordre_des_medecins",
        "description": "French regulator exposing RPPS identifiers, addresses, and specialties via GraphQL.",
        "access": "GraphQL POST requests to /graphql with session cookie + CSRF token.",
        "status": "todo",
    },
    {
        "slug": "bundesaerztekammer",
        "name": "Bundesarztekammer",
        "region": "Europe",
        "scope": "Germany",
        "raw_path": "data/raw/europe/germany/bundesaerztekammer",
        "description": "German federal body listing state chambers; orchestrates downstream scrapes.",
        "access": "Static HTML linking to each Landesaerztekammer portal.",
        "status": "todo",
    },
    {
        "slug": "big_register",
        "name": "BIG Register",
        "region": "Europe",
        "scope": "Netherlands",
        "raw_path": "data/raw/europe/netherlands/big_register",
        "description": "Dutch national register with REST API delivering BIG numbers and validity dates.",
        "access": "/api/Registrations with pagination tokens and Accept-Language header.",
        "status": "todo",
    },
    {
        "slug": "cgcom",
        "name": "Organizacion Medica Colegial",
        "region": "Europe",
        "scope": "Spain",
        "raw_path": "data/raw/europe/spain/organizacion_medica_colegial",
        "description": "Spanish national council integrating provincial colegiados lists.",
        "access": "Province-specific HTML/CSV endpoints; requires sequential access.",
        "status": "todo",
    },
    {
        "slug": "fnomceo",
        "name": "Federazione Nazionale degli Ordini dei Medici",
        "region": "Europe",
        "scope": "Italy",
        "raw_path": "data/raw/europe/italy/federazione_nazionale_degli_ordini_dei_medici",
        "description": "Italian federation exposing provincial order data through JSON APIs.",
        "access": "POST to /wp-json/fnomceo/v1/medici with nonce header.",
        "status": "todo",
    },
    {
        "slug": "ordem_dos_medicos",
        "name": "Ordem dos Medicos",
        "region": "Europe",
        "scope": "Portugal",
        "raw_path": "data/raw/europe/portugal/ordem_dos_medicos",
        "description": "Portuguese order with form-based lookup returning HTML records.",
        "access": "GET/POST workflows under /ver-medico/ with query params.",
        "status": "todo",
    },
    {
        "slug": "ordre_des_medecins",
        "name": "Ordre des Medecins (Belgium)",
        "region": "Europe",
        "scope": "Belgium",
        "raw_path": "data/raw/europe/belgium/ordre_des_medecins",
        "description": "Belgian order publishing bilingual listings requiring pagination crawls.",
        "access": "HTML listings at ordomedic.be with filter parameters.",
        "status": "todo",
    },
    {
        "slug": "medreg",
        "name": "MedReg",
        "region": "Europe",
        "scope": "Switzerland",
        "raw_path": "data/raw/europe/switzerland/medreg",
        "description": "Swiss federal register with REST API returning multilingual JSON payloads.",
        "access": "api/Medreg/v1/persons with optional API key.",
        "status": "todo",
    },
    {
        "slug": "socialstyrelsen",
        "name": "Socialstyrelsen",
        "region": "Europe",
        "scope": "Sweden",
        "raw_path": "data/raw/europe/nordic/socialstyrelsen",
        "description": "Swedish register accessible through JSON search, including authorization types.",
        "access": "POST to /api/search returning paginated JSON arrays.",
        "status": "todo",
    },
    {
        "slug": "valvira",
        "name": "Valvira",
        "region": "Europe",
        "scope": "Finland",
        "raw_path": "data/raw/europe/nordic/valvira",
        "description": "Finnish supervisory authority with CSV exports for healthcare professionals.",
        "access": "Downloadable CSV triggered by query parameters on valvira.fi.",
        "status": "todo",
    },
    {
        "slug": "danish_patient_safety_authority",
        "name": "Danish Patient Safety Authority",
        "region": "Europe",
        "scope": "Denmark",
        "raw_path": "data/raw/europe/nordic/danish_patient_safety_authority",
        "description": "Danish authorization register accessible via OData JSON endpoints.",
        "access": "/api/Authorisation with API key support and Retry-After headers.",
        "status": "todo",
    },
    {
        "slug": "norwegian_directorate_of_health",
        "name": "Norwegian Directorate of Health",
        "region": "Europe",
        "scope": "Norway",
        "raw_path": "data/raw/europe/nordic/norwegian_directorate_of_health",
        "description": "Norwegian HPR dataset distributed as daily CSV exports.",
        "access": "Download hpr-full dataset from data.helsedirektoratet.no.",
        "status": "todo",
    },
    {
        "slug": "ahpra",
        "name": "Australian Health Practitioner Regulation Agency",
        "region": "Oceania",
        "scope": "Australia",
        "raw_path": "data/raw/oceania/australia/australian_health_practitioner_regulation_agency",
        "description": "Australian regulator with JSON practitioner search covering conditions and scopes.",
        "access": "POST to /api/PractitionerSearch with pagination.",
        "status": "todo",
    },
    {
        "slug": "mcnz",
        "name": "Medical Council of New Zealand",
        "region": "Oceania",
        "scope": "New Zealand",
        "raw_path": "data/raw/oceania/new_zealand/medical_council_of_new_zealand",
        "description": "New Zealand council exposing register via JSON endpoint with scopes of practice.",
        "access": "/umbraco/api/register/search returning JSON payloads.",
        "status": "todo",
    },
    {
        "slug": "mhlw",
        "name": "Ministry of Health Labour and Welfare",
        "region": "Asia",
        "scope": "Japan",
        "raw_path": "data/raw/asia/japan/ministry_of_health_labour_and_welfare",
        "description": "Japanese ministry publishing aggregate physician statistics (no per-license rows).",
        "access": "Static PDF/XLS releases converted to CSV for reference.",
        "status": "todo",
    },
    {
        "slug": "kma",
        "name": "Korean Medical Association",
        "region": "Asia",
        "scope": "South Korea",
        "raw_path": "data/raw/asia/south_korea/korean_medical_association",
        "description": "Professional association list, useful as supplemental registry with CAPTCHA hurdles.",
        "access": "Member search portal requiring form POST and occasional CAPTCHA solving.",
        "status": "todo",
    },
    {
        "slug": "nmc",
        "name": "National Medical Commission",
        "region": "Asia",
        "scope": "India",
        "raw_path": "data/raw/asia/india/national_medical_commission",
        "description": "Indian national register accessible via REST endpoint returning JSON records.",
        "access": "MCIRest verifyDetails endpoint plus CAPTCHA token per session.",
        "status": "todo",
    },
    {
        "slug": "smc",
        "name": "Singapore Medical Council",
        "region": "Asia",
        "scope": "Singapore",
        "raw_path": "data/raw/asia/singapore/singapore_medical_council",
        "description": "Singapore regulator with searchable register listing register category and conditions.",
        "access": "prs.moh.gov.sg form POST returning HTML tables.",
        "status": "todo",
    },
    {
        "slug": "mchk",
        "name": "Medical Council of Hong Kong",
        "region": "Asia",
        "scope": "Hong Kong",
        "raw_path": "data/raw/asia/hong_kong/medical_council_of_hong_kong",
        "description": "Hong Kong council distributing XLS register exports for manual parsing.",
        "access": "Downloadable XLS/PDF register refreshed monthly.",
        "status": "todo",
    },
    {
        "slug": "israel_moh",
        "name": "Ministry of Health Israel",
        "region": "Middle East",
        "scope": "Israel",
        "raw_path": "data/raw/middle_east/israel/ministry_of_health_israel",
        "description": "Israeli practitioner portal with REST backend returning Hebrew metadata.",
        "access": "/api/Practitioner endpoints; requires locale-aware headers.",
        "status": "todo",
    },
    {
        "slug": "dha",
        "name": "Dubai Health Authority",
        "region": "Middle East",
        "scope": "United Arab Emirates (Dubai)",
        "raw_path": "data/raw/middle_east/united_arab_emirates/dubai_health_authority",
        "description": "Dubai licensing portal enumerating professionals, facilities, and license classes.",
        "access": "ASP.NET service ProfessionalSearchService.svc/GetProfessionals with throttling.",
        "status": "todo",
    },
    {
        "slug": "doh_abu_dhabi",
        "name": "Department of Health Abu Dhabi",
        "region": "Middle East",
        "scope": "United Arab Emirates (Abu Dhabi)",
        "raw_path": "data/raw/middle_east/united_arab_emirates/department_of_health_abu_dhabi",
        "description": "DOH Abu Dhabi public API listing licensed practitioners and facilities.",
        "access": "/api/publicsearch with JSON pagination and optional API key.",
        "status": "todo",
    },
    {
        "slug": "hpcsa",
        "name": "Health Professions Council of South Africa",
        "region": "Africa",
        "scope": "South Africa",
        "raw_path": "data/raw/africa/south_africa/health_professions_council_of_south_africa",
        "description": "South African regulator requiring CAPTCHA/FOI for bulk exports.",
        "access": "hpcsaonline.co.za form with CAPTCHA; prefer FOI export ingestion.",
        "status": "todo",
    },
    {
        "slug": "mdcn",
        "name": "Medical and Dental Council of Nigeria",
        "region": "Africa",
        "scope": "Nigeria",
        "raw_path": "data/raw/africa/nigeria/medical_and_dental_council_of_nigeria",
        "description": "Nigerian council offering verification API requiring CAPTCHA tokens.",
        "access": "portal.mdcngov.ng API /api/Practitioner/Verify.",
        "status": "todo",
    },
    {
        "slug": "kmpdc",
        "name": "Kenya Medical Practitioners and Dentists Council",
        "region": "Africa",
        "scope": "Kenya",
        "raw_path": "data/raw/africa/kenya/kenya_medical_practitioners_and_dentists_council",
        "description": "Kenyan council publishing PDF registers per profession.",
        "access": "Download PDF registers and convert to CSV.",
        "status": "todo",
    },
    {
        "slug": "cfm",
        "name": "Conselho Federal de Medicina",
        "region": "Latin America",
        "scope": "Brazil",
        "raw_path": "data/raw/latin_america/brazil/conselho_federal_de_medicina",
        "description": "Brazilian federal council offering AJAX search returning CRM numbers.",
        "access": "WP admin-ajax buscar_medicos endpoint with JSON payloads.",
        "status": "todo",
    },
    {
        "slug": "ministerio_salud_argentina",
        "name": "Ministerio de Salud Argentina",
        "region": "Latin America",
        "scope": "Argentina",
        "raw_path": "data/raw/latin_america/argentina/ministerio_de_salud_argentina",
        "description": "Argentinian REFEPS dataset accessible via authenticated API.",
        "access": "SOAP/REST hybrid requiring API key and token refresh.",
        "status": "todo",
    },
    {
        "slug": "superintendencia_salud",
        "name": "Superintendencia de Salud",
        "region": "Latin America",
        "scope": "Chile",
        "raw_path": "data/raw/latin_america/chile/superintendencia_de_salud",
        "description": "Chilean regulator providing XLS downloads per profession.",
        "access": "Download XLS registers listed on supersalud.gob.cl.",
        "status": "todo",
    },
    {
        "slug": "who",
        "name": "World Health Organization",
        "region": "International",
        "scope": "Global",
        "raw_path": "data/raw/international/meta/world_health_organization",
        "description": "WHO Global Health Observatory indicators for workforce density.",
        "access": "REST API at ghoapi.azureedge.net/api.",
        "status": "todo",
    },
    {
        "slug": "oecd",
        "name": "OECD",
        "region": "International",
        "scope": "OECD members",
        "raw_path": "data/raw/international/meta/oecd",
        "description": "OECD SDMX datasets for physician per capita metrics.",
        "access": "stats.oecd.org SDMX-JSON queries.",
        "status": "todo",
    },
    {
        "slug": "wdoms",
        "name": "World Directory of Medical Schools",
        "region": "International",
        "scope": "Global",
        "raw_path": "data/raw/international/meta/world_directory_of_medical_schools",
        "description": "School-level directory for training provenance joins.",
        "access": "search.wdoms.org GraphQL API (token required for bulk).",
        "status": "todo",
    },
]

FETCH_TEMPLATE = """\"\"\"Fetch utilities for {name}.\"\"\"

from __future__ import annotations

from pathlib import Path

RAW_DIR = Path(\"{raw_path}\")


def fetch_latest(*, output_dir: Path | None = None) -> Path:
    \"\"\"Download the latest {name} dataset and return the written path.\"\"\"
    target_dir = output_dir or RAW_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError(\"Implement fetch_latest for {slug}\")
"""

PARSE_TEMPLATE = """\"\"\"Parsing helpers for {name}.\"\"\"

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterator


def iter_records(raw_path: Path) -> Iterator[Dict[str, str]]:
    \"\"\"Yield canonicalized records extracted from the raw artifact.\"\"\"
    raise NotImplementedError(\"Implement iter_records for {slug}\")
"""

README_TEMPLATE = """# {name}

- Slug: `{slug}`
- Region: {region}
- Scope: {scope}
- Raw staging: `{raw_path}`

## Purpose
{description}

## Access Snapshot
{access}

## Implementation Checklist
1. Implement `fetch_latest()` to download and persist artifacts into `{raw_path}`
2. Implement `iter_records()` to parse raw payloads into canonical field names
3. Populate `mapping.yaml` with source→canonical field mappings
4. Add pytest coverage and wire the module into `src/pipeline`
"""

MAPPING_TEMPLATE = """# Placeholder mapping for {name}
# source_field: canonical_field
"""

INIT_TEMPLATE = """\"\"\"Source adapter for {name}.\"\"\"

from .fetch import fetch_latest
from .parse import iter_records

__all__ = [\"fetch_latest\", \"iter_records\"]
"""


def write_file_once(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def main() -> None:
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    for entry in SOURCES:
        module_dir = SOURCES_DIR / entry["slug"]
        if module_dir.exists():
            print(f"Skipping {entry['slug']}: already exists")
            continue
        module_dir.mkdir(parents=True, exist_ok=True)
        write_file_once(module_dir / "__init__.py", INIT_TEMPLATE.format(**entry))
        write_file_once(module_dir / "fetch.py", FETCH_TEMPLATE.format(**entry))
        write_file_once(module_dir / "parse.py", PARSE_TEMPLATE.format(**entry))
        write_file_once(module_dir / "mapping.yaml", MAPPING_TEMPLATE.format(**entry))
        write_file_once(module_dir / "README.md", README_TEMPLATE.format(**entry))
        print(f"Scaffolded {entry['slug']}")


if __name__ == "__main__":
    main()
