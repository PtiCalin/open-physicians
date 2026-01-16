# Norwegian Directorate of Health

- Region: Europe
- Country: Norway
- Coverage: Excellent national coverage

## Access
- URL: https://www.helsedirektoratet.no/registrene/hpr
- Access method: Download CSV via open data dataset `hpr-full`
- Recommended rate limit: Bulk export once daily; 100 MB file
- Authentication: None

## Legal & Compliance
- Reference: https://www.helsedirektoratet.no/om-oss/personvern
- Notes: Open data license NLOD; ensure attribution and change logs.

## Implementation Notes
- Store raw CSV compressed to save space
- Track dataset version and checksum
- Parse NOK-coded specialties
