import json

import httpx

from src.sources.cpsbc import fetch as cpsbc_fetch
from src.sources.cpsbc import parse as cpsbc_parse


def test_fetch_latest_cpsbc_collects_rows(tmp_path):
    responses = [
        {"results": [{"cpid": "A1"}], "has_more": False}
    ]
    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        assert request.method == "GET"
        call_count += 1
        return httpx.Response(200, json=responses[call_count - 1])

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport) as client:
        artifact_path = cpsbc_fetch.fetch_latest(output_dir=tmp_path, client=client)

    payload = json.loads(artifact_path.read_text(encoding="utf-8"))
    assert payload["source"] == "cpsbc"
    assert len(payload["results"]) == 1


def test_iter_records_cpsbc_normalizes_rows(tmp_path):
    sample = {
        "results": [
            {
                "cpid": "BC-999",
                "firstName": "Alex",
                "lastName": "Nguyen",
                "registration_status": "Practising",
                "specialty": "internal_medicine",
                "practiceProvince": "BC",
                "last_modified": "2024-03-15T12:00:00Z",
            }
        ]
    }
    raw_path = tmp_path / "cpsbc.json"
    raw_path.write_text(json.dumps(sample), encoding="utf-8")

    records = list(cpsbc_parse.iter_records(raw_path))
    assert records == [
        {
            "physician_id": "cpsbc-BC-999",
            "full_name": "Alex Nguyen",
            "license_status": "Practising",
            "specialty_code": "internal_medicine",
            "location_code": "CA-BC",
            "source": "cpsbc",
            "updated_at": "2024-03-15T12:00:00Z",
        }
    ]
