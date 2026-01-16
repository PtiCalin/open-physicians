# Federazione Nazionale degli Ordini dei Medici

- Region: Europe
- Country: Italy
- Coverage: Good national coverage

## Access
- URL: https://portale.fnomceo.it/ricerca-anagrafica/
- Access method: HTML search with underlying JSON POST at `/wp-json/fnomceo/v1/medici`
- Recommended rate limit: 1 request per second; rotate user agents for long runs
- Authentication: None, but uses nonce token in request headers

## Legal & Compliance
- Reference: https://portale.fnomceo.it/note-legali/
- Notes: Reuse allowed for transparency if source credited and context preserved.

## Implementation Notes
- Capture provincial order code and registration number
- Store raw Italian field labels for translators
- Track validation status for each physician
