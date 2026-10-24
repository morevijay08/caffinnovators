from fastapi.testclient import TestClient
from app.main import app
from app.services.career_catalogue import list_careers, get_career

client = TestClient(app)

def test_catalogue_has_unique_ids_and_approved_tags():
    careers = list_careers()
    assert len(careers) >= 10
    assert len({c["id"] for c in careers}) == len(careers)
    assert all(c["illustrative"] is True and c["interest_tags"] for c in careers)
    allowed = {"technology","science","design","writing","business","helping_people","environment","arts","mathematics","sports","problem_solving"}
    assert all(set(c["interest_tags"]) <= allowed for c in careers)

def test_get_catalogue_matches_schema():
    response = client.get("/api/v1/careers")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == len(data["careers"]) == 12
    assert "technology" in data["clusters"]

def test_case_insensitive_search():
    response = client.get("/api/v1/careers", params={"search":"ROBOT"})
    assert response.status_code == 200
    assert any(c["id"] == "robotics-technician" for c in response.json()["careers"])

def test_cluster_filter():
    result = client.get("/api/v1/careers", params={"cluster":"creative"}).json()
    assert result["careers"]
    assert all(c["cluster"] == "creative" for c in result["careers"])

def test_combined_filters_and_empty_results():
    response = client.get("/api/v1/careers", params={"cluster":"sports","search":"illustrator"})
    assert response.status_code == 200
    assert response.json()["total"] == 0
    assert response.json()["careers"] == []

def test_detail_and_unknown_id():
    career = client.get("/api/v1/careers/software-developer")
    assert career.status_code == 200
    assert career.json()["id"] == "software-developer"
    assert get_career("missing") is None
    missing = client.get("/api/v1/careers/missing")
    assert missing.status_code == 404

def test_query_validation():
    assert client.get("/api/v1/careers", params={"search":"x"*101}).status_code == 422
