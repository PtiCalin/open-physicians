# College of Physicians and Surgeons of Ontario

- Region: North America
- Country: Canada
- Coverage: Excellent, provincial but consistent

## Access
- URL: https://doctors.cpso.on.ca/
- Access method: HTML search endpoint with JSON POST (GetDoctors) payloads for pagination
- Recommended rate limit: 1 request per second per endpoint; rotate user agents hourly
- Authentication: None, but anti-bot JavaScript requires realistic headers

## Legal & Compliance
- Reference: https://www.cpso.on.ca/Footer-Pages/Privacy/Terms-of-Use
- Notes: CPSO restricts commercial reuse; cite CPSO and include retrieval date.

## Implementation Notes
- Persist raw JSON pages before normalization
- Capture physician profile URLs for deep-link verification
- Reconcile CPSO number to canonical physician_id
