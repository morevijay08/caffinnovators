"""Persistence and retrieval tests for TASK-009A using isolated temporary SQLite."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.api.math_assessment import router
from app.db import Base, get_db
from app.main import app
from app.models.assessment_attempt import AssessmentAttempt
from app.data.math_questions import QUESTION_BANK


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client, TestingSessionLocal
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_submit_persists_attempt_and_get_retrieves_same_result(client):
    test_client, session_factory = client
    response = test_client.post(
        "/api/v1/math-assessment/submit",
        json={
            "answers": [{"question_id": "math-001", "option_id": "b"}],
            "elapsed_seconds": 60,
        },
    )
    assert response.status_code == 200
    submitted = response.json()
    assert submitted["attempt_id"]
    assert submitted["correct_answers"] == 1
    assert submitted["topic_breakdown"]

    with session_factory() as db:
        count = db.scalar(select(func.count()).select_from(AssessmentAttempt))
    assert count == 1

    retrieved = test_client.get(
        f"/api/v1/math-assessment/attempts/{submitted['attempt_id']}"
    )
    assert retrieved.status_code == 200
    assert retrieved.json() == submitted


def test_unknown_attempt_returns_404(client):
    test_client, _ = client
    response = test_client.get(
        "/api/v1/math-assessment/attempts/00000000-0000-4000-8000-000000000000"
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Assessment attempt not found."


@pytest.mark.parametrize(
    "answers",
    [
        [{"question_id": "missing", "option_id": "a"}],
        [
            {"question_id": "math-001", "option_id": "b"},
            {"question_id": "math-001", "option_id": "b"},
        ],
        [{"question_id": "math-001", "option_id": "invalid"}],
    ],
)
def test_invalid_submission_is_not_persisted(client, answers):
    test_client, session_factory = client
    response = test_client.post(
        "/api/v1/math-assessment/submit",
        json={"answers": answers, "elapsed_seconds": 20},
    )
    assert response.status_code == 422
    with session_factory() as db:
        count = db.scalar(select(func.count()).select_from(AssessmentAttempt))
    assert count == 0


def test_persisted_attempt_survives_session_close_and_reopen(client):
    test_client, session_factory = client
    response = test_client.post(
        "/api/v1/math-assessment/submit",
        json={
            "answers": [
                {"question_id": question.id, "option_id": question.correct_option_id}
                for question in QUESTION_BANK
            ],
            "elapsed_seconds": 300,
        },
    )
    assert response.status_code == 200
    attempt_id = response.json()["attempt_id"]

    with session_factory() as first_session:
        assert first_session.get(AssessmentAttempt, attempt_id) is not None
    with session_factory() as reopened_session:
        record = reopened_session.get(AssessmentAttempt, attempt_id)
        assert record is not None
        assert record.correct_answers == len(QUESTION_BANK)
