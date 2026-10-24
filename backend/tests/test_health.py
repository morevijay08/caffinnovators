from fastapi.testclient import TestClient
from app.main import app


def test_health_contract():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "lifepath-api"}


def test_implemented_career_catalogue_is_exposed():
    response = TestClient(app).get("/api/v1/careers")
    assert response.status_code == 200
    assert response.json()["total"] > 0
