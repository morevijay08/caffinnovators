from fastapi.testclient import TestClient
from app.main import app


def test_health_contract():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "lifepath-api"}


def test_unimplemented_feature_is_not_exposed():
    assert TestClient(app).get("/api/v1/careers").status_code == 404
