# Australian Health Practitioner Regulation Agency

- Region: Oceania
- Country: Australia
- Coverage: Excellent national coverage

## Access
- URL: https://www.ahpra.gov.au/Registration/Registers-of-Practitioners.aspx
- Access method: Public search hitting `/api/PractitionerSearch` JSON endpoint
- Recommended rate limit: 2 requests per second; nightly batches only
- Authentication: None

## Legal & Compliance
- Reference: https://www.ahpra.gov.au/Footer/Privacy.aspx
- Notes: Use data for transparency; do not imply AHPRA endorsement.

## Implementation Notes
- Capture conditions and undertakings
- Track registration type and division
- Align AHPRA numbers with canonical IDs
