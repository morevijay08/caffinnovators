"""TASK-018 cross-feature smoke checks against the task-series FastAPI app.

These checks exercise the real API router contracts using an in-process
TestClient. Frontend browser navigation is verified separately in the review.
"""
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def _answers():
    response = client.get("/api/v1/interest-assessment")
    assert response.status_code == 200
    data = response.json()
    assert data["duration_seconds"] > 0
    questions = data["questions"]
    assert len(questions) == 6
    assert all(len(q["options"]) >= 2 for q in questions)
    assert "signals" not in str(questions)
    return [
        {"question_id": q["id"], "option_id": q["options"][0]["id"]}
        for q in questions
    ]


def test_student_discovery_journey_across_endpoints():
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json() == {"status": "ok", "service": "lifepath-api"}

    careers = client.get("/api/v1/careers")
    assert careers.status_code == 200
    catalogue = careers.json()["careers"]
    assert len(catalogue) >= 5
    ids = {career["id"] for career in catalogue}
    assert len(ids) == len(catalogue)
    assert all(career["illustrative"] for career in catalogue)

    answers = _answers()
    assessment = client.post("/api/v1/interest-assessment/submit", json={"answers": answers})
    assert assessment.status_code == 200
    assert assessment.json()["signals"]

    recommendation = client.post("/api/v1/recommendations", json={"answers": answers, "limit": 3})
    assert recommendation.status_code == 200
    result = recommendation.json()
    assert len(result["recommendations"]) == 3
    assert result["assessment_signals"] == assessment.json()["signals"]
    scores = [career["match_score"] for career in result["recommendations"]]
    assert scores == sorted(scores, reverse=True)

    for career in result["recommendations"]:
        assert career["career_id"] in ids
        assert career["explanation"]
        assert career["suggested_steps"]
        detail = client.get("/api/v1/careers/" + career["career_id"])
        assert detail.status_code == 200
        assert detail.json()["id"] == career["career_id"]
        assert detail.json()["illustrative"] is True


def test_invalid_or_missing_resources_have_safe_errors():
    answers = _answers()
    incomplete = answers[:-1]
    assessment = client.post("/api/v1/interest-assessment/submit", json={"answers": incomplete})
    assert assessment.status_code == 422
    assert "detail" in assessment.json()

    recommendation = client.post("/api/v1/recommendations", json={"answers": incomplete})
    assert recommendation.status_code == 422
    assert "detail" in recommendation.json()

    unknown_career = client.get("/api/v1/careers/unknown-demo-career")
    assert unknown_career.status_code == 404
    assert "detail" in unknown_career.json()


def test_catalogue_filtering_and_consistent_detail():
    unfiltered = client.get("/api/v1/careers")
    assert unfiltered.status_code == 200
    all_items = unfiltered.json()["careers"]

    filtered = client.get("/api/v1/careers", params={"cluster": "technology"})
    assert filtered.status_code == 200
    found = filtered.json()["careers"]
    assert found and len(found) < len(all_items)
    assert all(item["cluster"] == "technology" for item in found)

    for item in found:
        detail = client.get("/api/v1/careers/" + item["id"])
        assert detail.status_code == 200
        assert detail.json()["title"] == item["title"]
