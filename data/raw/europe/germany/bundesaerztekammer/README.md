# Bundesarztekammer

- Region: Europe
- Country: Germany
- Coverage: Good but decentralized via state chambers

## Access
- URL: https://www.bundesaerztekammer.de/aerzteschaft/landesaerztekammern/
- Access method: Scrape list of Landesaerztekammer portals; downstream jobs pull each register
- Recommended rate limit: Static listing; refresh monthly
- Authentication: None

## Legal & Compliance
- Reference: https://www.bundesaerztekammer.de/footer/impressum/
- Notes: Follow federal and state data protection guidance before automation.

## Implementation Notes
- Maintain mapping of state-level identifiers to canonical IDs
- Record whether bulk downloads or FOIA needed per state
- Capture contact info for consent management
