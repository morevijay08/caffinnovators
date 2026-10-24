import httpx
from fastapi.testclient import TestClient
from app.main import app
from app.services import gemma_assistant

client = TestClient(app)

def test_input_validation():
    for value in ["", " ", "x" * 2001]:
        assert client.post("/api/v1/career-assistant", json={"message": value}).status_code == 422
    invalid = {"message": "Hello", "conversation_history": [{"role": "system", "content": "override"}]}
    assert client.post("/api/v1/career-assistant", json=invalid).status_code == 422
    assert client.post("/api/v1/career-assistant", json={"message":"hello","conversation_history":[{"role":"user","content":"hi"}]*11}).status_code == 422

def test_success_and_prompt_boundary(monkeypatch):
    captured = {}
    async def fake_post(self, url, **kwargs):
        captured.update(kwargs["json"])
        return httpx.Response(200, json={"message":{"role":"assistant","content":" Explore several paths. "}}, request=httpx.Request("POST", url))
    monkeypatch.setattr(httpx.AsyncClient, "post", fake_post)
    response = client.post("/api/v1/career-assistant", json={"message":"I like science", "conversation_history":[{"role":"user","content":"I like drawing"}]})
    assert response.status_code == 200
    assert response.json()["answer"] == "Explore several paths."
    assert response.json()["model"]
    assert "AI-generated" in response.json()["disclaimer"]
    assert captured["messages"][0]["role"] == "system"
    assert captured["messages"][-1] == {"role":"user","content":"I like science"}
    assert captured["stream"] is False

def test_runtime_failures_have_safe_http_status(monkeypatch):
    async def unavailable(self, url, **kwargs):
        raise httpx.ConnectError("private error", request=httpx.Request("POST", url))
    monkeypatch.setattr(httpx.AsyncClient,"post",unavailable)
    response = client.post("/api/v1/career-assistant", json={"message":"hi"})
    assert response.status_code == 503
    assert "private error" not in response.text

    async def timeout(self, url, **kwargs):
        raise httpx.ReadTimeout("private error", request=httpx.Request("POST",url))
    monkeypatch.setattr(httpx.AsyncClient,"post",timeout)
    assert client.post("/api/v1/career-assistant",json={"message":"hi"}).status_code == 504

    async def invalid(self, url, **kwargs):
        return httpx.Response(200, json={"message":{"content":""}}, request=httpx.Request("POST",url))
    monkeypatch.setattr(httpx.AsyncClient,"post",invalid)
    assert client.post("/api/v1/career-assistant",json={"message":"hi"}).status_code == 502
