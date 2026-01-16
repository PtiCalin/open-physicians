# College of Physicians and Surgeons of British Columbia

- Region: North America
- Country: Canada
- Coverage: Excellent, provincial but consistent

## Access
- URL: https://www.cpsbc.ca/physician_directory
- Access method: Form-based search backed by JSON API (endpoint /physician_directory/search)
- Recommended rate limit: 0.5 requests per second; rotate IP if blocked
- Authentication: None; include Referer header matching cpsbc.ca

## Legal & Compliance
- Reference: https://www.cpsbc.ca/terms-use
- Notes: Follow CPSBC terms forbidding misuse or misrepresentation of register data.

## Implementation Notes
- Archive request payloads for reproducibility
- Capture status history when available
- Map CPSBC specialties to canonical codes
