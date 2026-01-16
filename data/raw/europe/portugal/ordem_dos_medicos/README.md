# Ordem dos Medicos

- Region: Europe
- Country: Portugal
- Coverage: Good national coverage

## Access
- URL: https://www.ordemdosmedicos.pt/ver-medico/
- Access method: Search form posting to `/ver-medico/` with query parameters
- Recommended rate limit: 1 request per second; respect caching headers
- Authentication: None

## Legal & Compliance
- Reference: https://www.ordemdosmedicos.pt/politica-de-privacidade/
- Notes: Portuguese privacy policy requires attribution and lawful purpose.

## Implementation Notes
- Normalize OM numbers
- Translate specialty strings to canonical codes
- Capture public disciplinary notes when present
