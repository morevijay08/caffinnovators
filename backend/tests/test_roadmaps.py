from fastapi.testclient import TestClient
from app.main import app
from app.services.career_roadmaps import get_career_roadmap

client = TestClient(app)

def test_all_catalogue_careers_have_unique_illustrative_roadmaps():
    careers = client.get("/api/v1/careers").json()["careers"]
    assert len(careers) == 12
    for career in careers:
        response = client.get(f"/api/v1/careers/{career['id']}/roadmap")
        assert response.status_code == 200
        roadmap = response.json()
        assert roadmap["career_id"] == career["id"]
        assert roadmap["career_title"] == career["title"]
        assert roadmap["illustrative"] is True
        assert roadmap["duration_years"] == len(roadmap["years"]) == 4
        assert [year["year"] for year in roadmap["years"]] == [1, 2, 3, 4]
        assert all(year["activities"] and year["milestone"] and year["focus"] for year in roadmap["years"])
        assert "illustrative" in roadmap["disclaimer"].lower()

def test_unknown_career_roadmap_returns_safe_404():
    response = client.get("/api/v1/careers/unknown-career/roadmap")
    assert response.status_code == 404
    assert response.json()["detail"] == "Career roadmap not found in the illustrative catalogue."

def test_roadmap_is_deterministic_and_not_mutated():
    first = get_career_roadmap("software-developer")
    second = get_career_roadmap("software-developer")
    assert first == second
    assert first is not second
    assert first["years"][0]["milestone"] != get_career_roadmap("sports-coach")["years"][0]["milestone"]
