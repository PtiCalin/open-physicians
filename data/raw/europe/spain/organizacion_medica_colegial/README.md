# Organizacion Medica Colegial

- Region: Europe
- Country: Spain
- Coverage: Good national coverage

## Access
- URL: https://www.cgcom.es/colegiados
- Access method: HTML form posts to provincial council endpoints; requires per-college scraping
- Recommended rate limit: 1 request per 3 seconds per provincial endpoint
- Authentication: None

## Legal & Compliance
- Reference: https://www.cgcom.es/aviso-legal
- Notes: Respect Spanish data reuse law and cite CGCOM.

## Implementation Notes
- Track which colegios provide bulk CSV
- Normalize collegiate numbers and province codes
- Document gaps for provinces lacking automation
