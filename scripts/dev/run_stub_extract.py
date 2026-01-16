"""Developer helper to exercise the extract stage with local stub data."""
from __future__ import annotations

from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.pipeline import extract


def _write_json(path: Path, payload: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _write_csv(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def cmq_stub() -> Path:
    return _write_csv(Path("data/raw/cmq/cmq_stub.csv"), "physician_id,full_name\n")


def cpso_stub() -> Path:
    payload = {
        "results": [
            {
                "registrationNumber": "99999",
                "fullName": "Test Doctor",
                "registrationStatus": "Active",
            }
        ]
    }
    return _write_json(
        Path(
            "data/raw/north_america/canada/"
            "college_of_physicians_and_surgeons_of_ontario/cpso_stub.json"
        ),
        payload,
    )


def cpsbc_stub() -> Path:
    payload = {
        "results": [
            {
                "cpid": "BC-STUB",
                "firstName": "Test",
                "lastName": "Physician",
                "registration_status": "Practising",
                "specialty": "family_medicine",
            }
        ]
    }
    return _write_json(
        Path(
            "data/raw/north_america/canada/"
            "college_of_physicians_and_surgeons_of_british_columbia/cpsbc_stub.json"
        ),
        payload,
    )


if __name__ == "__main__":
    extract.run(fetch_overrides={"cmq": cmq_stub, "cpso": cpso_stub, "cpsbc": cpsbc_stub})
