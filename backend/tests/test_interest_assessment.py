from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_questions_have_no_answer_signals():
    response = client.get("/api/v1/interest-assessment")
    assert response.status_code == 200
    questions = response.json()["questions"]
    assert len(questions) == 6
    assert "signals" not in str(questions)
    assert all(len(q["options"]) == 3 for q in questions)

def test_deterministic_submission_and_explanation():
    questions = client.get("/api/v1/interest-assessment").json()["questions"]
    answers = [{"question_id": q["id"], "option_id": q["options"][0]["id"]} for q in questions]
    one = client.post("/api/v1/interest-assessment/submit", json={"answers": answers})
    two = client.post("/api/v1/interest-assessment/submit", json={"answers": answers})
    assert one.status_code == 200
    assert one.json() == two.json()
    assert one.json()["signals"]
    assert one.json()["top_interests"]
    assert all(0 <= s["score"] <= 100 for s in one.json()["signals"])

def test_reject_missing_duplicate_and_unknown_options():
    questions = client.get("/api/v1/interest-assessment").json()["questions"]
    valid = [{"question_id": q["id"], "option_id": q["options"][0]["id"]} for q in questions]
    for answers in [valid[:-1], valid[:-1] + [valid[0]], [{**valid[0], "option_id":"invalid"}] + valid[1:]]:
        assert client.post("/api/v1/interest-assessment/submit", json={"answers": answers}).status_code == 422

def test_reject_empty_payload():
    assert client.post("/api/v1/interest-assessment/submit", json={"answers":[]}).status_code == 422


def test_repeated_quizzes_rotate_questions_and_still_score():
    sets = [client.get("/api/v1/interest-assessment").json()["questions"] for _ in range(3)]
    assert all(len(questions) == 6 for questions in sets)
    assert len({tuple(q["prompt"] for q in questions) for questions in sets}) == 3
    for questions in sets:
        answers = [{"question_id":q["id"],"option_id":q["options"][0]["id"]} for q in questions]
        scored = client.post("/api/v1/interest-assessment/submit",json={"answers":answers})
        assert scored.status_code == 200
        recommended = client.post("/api/v1/recommendations",json={"answers":answers,"limit":3})
        assert recommended.status_code == 200


def test_reject_mix_of_two_questions_from_same_slot():
    from app.data.interest_questions import QUESTION_SETS
    questions = QUESTION_SETS[0]
    answers = [{"question_id":q["id"],"option_id":q["options"][0]["id"]} for q in questions]
    answers[1] = {"question_id":QUESTION_SETS[1][0]["id"],"option_id":QUESTION_SETS[1][0]["options"][0]["id"]}
    assert client.post("/api/v1/interest-assessment/submit",json={"answers":answers}).status_code == 422
