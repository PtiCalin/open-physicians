import json

import httpx

from src.sources.cpso import fetch as cpso_fetch
from src.sources.cpso import parse as cpso_parse


def test_fetch_latest_cpso_aggregates_pages(tmp_path):
    responses = [
        {"results": [{"registrationNumber": "111"}], "hasMore": True},
        {"results": [{"registrationNumber": "222"}], "hasMore": False},
    ]
    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        assert request.method == "POST"
        call_count += 1
        return httpx.Response(200, json=responses[call_count - 1])

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport) as client:
        artifact_path = cpso_fetch.fetch_latest(output_dir=tmp_path, client=client, max_pages=2)

    payload = json.loads(artifact_path.read_text(encoding="utf-8"))
    assert payload["source"] == "cpso"
    assert len(payload["results"]) == 2


def test_iter_records_cpso_normalizes_rows(tmp_path):
    sample = {
        "results": [
            {
                "registrationNumber": "12345",
                "fullName": "DOE, JANE",
                "registrationStatus": "Active",
                "primarySpecialty": "cardiology",
                "practiceLocation": {"province": "ON"},
                "lastUpdated": "2024-05-01T00:00:00Z",
            }
        ]
    }
    raw_path = tmp_path / "cpso.json"
    raw_path.write_text(json.dumps(sample), encoding="utf-8")

    records = list(cpso_parse.iter_records(raw_path))
    assert records == [
        {
            "physician_id": "cpso-12345",
            "full_name": "Doe, Jane",
            "license_status": "Active",
            "specialty_code": "cardiology",
            "location_code": "CA-ON",
            "source": "cpso",
            "updated_at": "2024-05-01T00:00:00Z",
        }
    ]
