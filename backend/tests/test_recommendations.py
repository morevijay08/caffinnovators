from fastapi.testclient import TestClient
from app.main import app
from app.services.career_recommendations import recommend_from_answers

client = TestClient(app)

def sample_answers(option: str = "a"):
    questions = client.get("/api/v1/interest-assessment").json()["questions"]
    return [{"question_id": q["id"], "option_id": option} for q in questions]

def test_ranked_explainable_career_ids():
    response = client.post("/api/v1/recommendations", json={"answers": sample_answers()})
    assert response.status_code == 200
    data = response.json()
    items = data["recommendations"]
    assert len(items) == 5
    assert all(item["explanation"] and item["suggested_steps"] for item in items)
    assert all(item["illustrative"] and 0 <= item["match_score"] <= 100 for item in items)
    assert [i["match_score"] for i in items] == sorted([i["match_score"] for i in items], reverse=True)
    valid_ids = {c["id"] for c in client.get("/api/v1/careers").json()["careers"]}
    assert all(i["career_id"] in valid_ids for i in items)

def test_determinism_and_limit():
    first = recommend_from_answers(sample_answers(), 3)
    second = recommend_from_answers(sample_answers(), 3)
    assert first == second and len(first["recommendations"]) == 3

def test_different_answers_change_signals():
    a = recommend_from_answers(sample_answers("a"))
    b = recommend_from_answers(sample_answers("b"))
    assert a["assessment_signals"] != b["assessment_signals"]

def test_reject_missing_duplicate_unknown():
    answers = sample_answers()
    variants = [answers[:-1], answers[:-1] + [answers[0]], [{**answers[0],"option_id":"z"}]+answers[1:]]
    for bad in variants:
        assert client.post("/api/v1/recommendations",json={"answers":bad}).status_code == 422

def test_reject_bad_limit():
    for limit in [0,13]:
        assert client.post("/api/v1/recommendations",json={"answers":sample_answers(),"limit":limit}).status_code == 422
