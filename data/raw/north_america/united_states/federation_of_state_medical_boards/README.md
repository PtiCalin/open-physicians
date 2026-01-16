# Federation of State Medical Boards

- Region: North America
- Country: United States
- Coverage: High but fragmented; acts as an index

## Access
- URL: https://www.fsmb.org/contact-a-state-medical-board/
- Access method: Static HTML directory; scrape board metadata and licensing URLs
- Recommended rate limit: Static page; single fetch per release
- Authentication: None

## Legal & Compliance
- Reference: https://www.fsmb.org/terms-of-use/
- Notes: FSMB material is informational; respect copyrights on proprietary reports.

## Implementation Notes
- Use output to drive per-state job scheduling
- Include contact emails and phone numbers for escalation
- Track state portal authentication requirements
