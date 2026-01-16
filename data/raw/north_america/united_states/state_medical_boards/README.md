# United States State Medical Boards

- Region: North America
- Country: United States
- Coverage: High, but each board varies in format and cadence

## Access
- URL: https://www.fsmb.org/contact-a-state-medical-board/
- Access method: Refer to individual board portals (CSV, HTML, PDF, or SOAP APIs)
- Recommended rate limit: Default to 1 request per second per board until policy reviewed
- Authentication: Varies: some require CAPTCHA or portal accounts

## Legal & Compliance
- Reference: Board-specific terms (see respective portal footers)
- Notes: Confirm statutory allowances for automated access before scraping each board.

## Implementation Notes
- Create subdirectories per state abbreviation
- Store portal policy snapshots for compliance audits
- Document blockers (CAPTCHA, paywalls, FOIA only)
