# Ordre des Medecins (Belgium)

- Region: Europe
- Country: Belgium
- Coverage: Good national coverage

## Access
- URL: https://www.ordomedic.be/fr/medecins/registre
- Access method: Server-rendered HTML list with filters; requires pagination crawling
- Recommended rate limit: 1 request every 2 seconds; site blocks aggressive bots
- Authentication: None

## Legal & Compliance
- Reference: https://www.ordomedic.be/fr/disclaimer
- Notes: Respect bilingual presentation and cite Ordre/Orde appropriately.

## Implementation Notes
- Capture both French and Dutch field variants
- Map national numbers to canonical IDs
- Preserve specialty board memberships
