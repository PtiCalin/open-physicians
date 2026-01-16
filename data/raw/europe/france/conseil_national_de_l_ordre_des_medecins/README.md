# Conseil National de l'Ordre des Medecins

- Region: Europe
- Country: France
- Coverage: Excellent with rich physician detail

## Access
- URL: https://www.conseil-national.medecin.fr/le-tableau
- Access method: GraphQL API powering tableau search; inspect network calls to `/graphql`
- Recommended rate limit: 1 request per second; abide by rate headers
- Authentication: Session cookie plus CSRF token

## Legal & Compliance
- Reference: https://www.conseil-national.medecin.fr/mentions-legales
- Notes: Data protected by French reuse rules; cite CNOM and respect GDPR obligations.

## Implementation Notes
- Store French-language fields plus normalized English equivalents
- Capture practice addresses and RPPS identifiers
- Add job to translate specialty labels to canonical codes
