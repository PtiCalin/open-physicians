# General Medical Council

- Region: Europe
- Country: United Kingdom
- Coverage: Excellent national register

## Access
- URL: https://www.gmc-uk.org/registration-and-licensing/the-medical-register
- Access method: JSON API (`/api/gmc/Registrations`) backing advanced search
- Recommended rate limit: 5 requests per second allowed; keep concurrency <=2
- Authentication: None; include standard browser headers

## Legal & Compliance
- Reference: https://www.gmc-uk.org/using-our-site/website-terms-and-conditions
- Notes: Reuse permitted for transparency with attribution; no implying GMC endorsement.

## Implementation Notes
- Fetch by alphabetical batch to avoid missing records
- Capture license status history and sanctions
- Map GMC reference number to canonical IDs
