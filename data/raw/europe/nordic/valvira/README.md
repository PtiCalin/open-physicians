# Valvira

- Region: Europe
- Country: Finland
- Coverage: Excellent national coverage

## Access
- URL: https://www.valvira.fi/web/en/healthcare/professional_practice_rights/register
- Access method: CSV export triggered via query parameters; fallback to HTML parsing
- Recommended rate limit: 1 export per minute; portal queues longer jobs
- Authentication: None

## Legal & Compliance
- Reference: https://www.valvira.fi/web/en/site-terms-of-use
- Notes: Follow Finnish PSI rules and ensure GDPR-compliant storage.

## Implementation Notes
- Capture professional right type and validity ranges
- Preserve bilingual Finnish/Swedish labels
- Record export query parameters in metadata
