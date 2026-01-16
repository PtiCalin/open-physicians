# BIG Register

- Region: Europe
- Country: Netherlands
- Coverage: Excellent national register

## Access
- URL: https://www.bigregister.nl/zoek-zorgverlener
- Access method: JSON API `/api/Registrations` with pagination tokens
- Recommended rate limit: 2 requests per second; throttle harder during business hours
- Authentication: None, but requires Accept-Language header

## Legal & Compliance
- Reference: https://www.bigregister.nl/footer/disclaimer
- Notes: Reuse allowed with attribution and without altering context.

## Implementation Notes
- Capture BIG number, profession, and validity dates
- Record language of response for audit
- Normalize municipality codes
