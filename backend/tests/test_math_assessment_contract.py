"""TASK-017 contract and regression checks for the math readiness API.

These tests intentionally verify public API behavior rather than internal implementation.
The TestClient uses the app's configured test/runtime database; attempts are anonymous.
"""
from uuid import UUID

import pytest

from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture(autouse=True, scope="module")
def run_app_lifespan():
    """Initialize the SQLite schema through the app startup lifecycle."""
    with TestClient(app) as client:
        globals()["client"] = client
        yield
    globals().pop("client", None)


def _assessment():
    response = client.get("/api/v1/math-assessment")
    assert response.status_code == 200
    return response.json()


def _all_correct_answers(assessment):
    # Correct answers are deliberately not exposed by GET. This helper chooses
    # a valid option to verify contract/scoring behavior without assuming keys.
    return [
        {"question_id": question["id"], "option_id": question["options"][0]["id"]}
        for question in assessment["questions"]
    ]


def test_math_assessment_public_contract_hides_answer_keys():
    response = client.get("/api/v1/math-assessment")
    assert response.status_code == 200
    data = response.json()
    assert data["assessment_id"]
    assert data["duration_seconds"] > 0
    assert data["question_count"] == len(data["questions"])
    assert data["illustrative"] is True
    assert data["questions"]
    for question in data["questions"]:
        assert question["id"] and question["prompt"]
        assert question["topic"] and question["topic_label"]
        assert len(question["options"]) >= 2
        assert all(set(option) == {"id", "text"} for option in question["options"])
        assert "correct_option_id" not in question
        assert "explanation" not in question


def test_math_submission_returns_consistent_topic_breakdown_and_persisted_attempt():
    assessment = _assessment()
    answers = _all_correct_answers(assessment)
    response = client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": answers, "elapsed_seconds": 42},
    )
    assert response.status_code == 200
    result = response.json()
    assert result["attempt_id"]
    UUID(result["attempt_id"])
    assert result["assessment_id"] == assessment["assessment_id"]
    assert result["total_questions"] == assessment["question_count"]
    assert result["answered_questions"] == len(answers)
    assert result["correct_answers"] + result["incorrect_or_unanswered"] == result["total_questions"]
    assert 0 <= result["percentage"] <= 100
    assert result["elapsed_seconds"] == 42
    assert result["time_limit_exceeded"] is False
    assert result["topic_breakdown"]
    assert sum(topic["total"] for topic in result["topic_breakdown"]) == result["total_questions"]
    assert sum(topic["correct"] for topic in result["topic_breakdown"]) == result["correct_answers"]
    for topic in result["topic_breakdown"]:
        assert topic["total"] > 0
        assert 0 <= topic["correct"] <= topic["total"]
        assert 0 <= topic["percentage"] <= 100

    history = client.get(f"/api/v1/math-assessment/attempts/{result['attempt_id']}")
    assert history.status_code == 200
    assert history.json() == result


def test_math_submission_rejects_unknown_duplicate_and_invalid_answers():
    assessment = _assessment()
    first = assessment["questions"][0]
    valid_option = first["options"][0]["id"]

    unknown = client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": [{"question_id": "unknown-question", "option_id": valid_option}],
              "elapsed_seconds": 0},
    )
    assert unknown.status_code == 422

    duplicate = client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": [
            {"question_id": first["id"], "option_id": valid_option},
            {"question_id": first["id"], "option_id": valid_option},
        ], "elapsed_seconds": 0},
    )
    assert duplicate.status_code == 422

    invalid_option = client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": [{"question_id": first["id"], "option_id": "not-an-option"}],
              "elapsed_seconds": 0},
    )
    assert invalid_option.status_code == 422


def test_math_attempt_history_returns_safe_not_found_for_unknown_uuid():
    response = client.get("/api/v1/math-assessment/attempts/00000000-0000-4000-8000-000000000000")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_math_submission_validates_elapsed_time_at_schema_boundary():
    assessment = _assessment()
    answer = _all_correct_answers(assessment)[0]
    response = client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": [answer], "elapsed_seconds": -1},
    )
    assert response.status_code == 422
