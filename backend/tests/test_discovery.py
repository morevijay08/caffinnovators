from fastapi.testclient import TestClient
from app.main import app
from app.data.discovery_activities import get_activities

client = TestClient(app)

def test_discovery_activity_listing():
    response = client.get("/api/v1/discovery-activities")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == len(data["activities"]) == 6
    assert all(a["illustrative"] and a["instructions"] and a["reflection_prompt"] for a in data["activities"])

def test_filtering_is_case_insensitive():
    response = client.get("/api/v1/discovery-activities", params={"interest":"SCIENCE"})
    assert response.status_code == 200
    assert response.json()["total"] >= 1
    assert all("science" in a["interest_tags"] for a in response.json()["activities"])

def test_unknown_and_invalid_filters():
    assert client.get("/api/v1/discovery-activities", params={"interest":"unknown"}).json()["total"] == 0
    assert client.get("/api/v1/discovery-activities", params={"interest":"x"*41}).status_code == 422

def test_returns_independent_copies():
    first = get_activities()
    first[0]["instructions"].append("changed")
    assert "changed" not in get_activities()[0]["instructions"]
