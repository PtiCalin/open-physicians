# Schema Notes

The canonical JSON Schema for physician records lives in `schemas/physician.schema.json`. This document highlights modeling decisions:

- Identifiers follow a ULID string for sortability
- Country and region codes leverage ISO-3166 alpha-2
- Status enumerations prefer descriptive strings over numeric flags
- Nested contact information remains optional due to source gaps
