"""Auth and persistence regression coverage without running Ollama."""
from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

def new_user(client:TestClient):
    credentials={"username":"student_"+uuid4().hex[:12],"password":"correct_horse_2026"}
    result=client.post("/api/v1/auth/register",json=credentials)
    assert result.status_code==201, result.text
    assert "httponly" in result.headers["set-cookie"].lower()
    assert "password" not in result.text.lower()
    return credentials

def test_registration_login_restore_and_logout():
    with TestClient(app) as client:
        assert client.get("/api/v1/journey").status_code==401
        credentials=new_user(client)
        state=client.get("/api/v1/journey")
        assert state.status_code==200
        assert state.json()["profile"] is None
        profile={"educationLevel":"Class 10","interests":["Technology"],"favoriteSubjects":["Mathematics"],"goal":"Explore career options","careerIdea":""}
        assert client.patch("/api/v1/journey",json={"field":"profile","value":profile}).status_code==200
        assert client.patch("/api/v1/journey",json={"field":"selectedCareerId","value":"software-developer"}).status_code==200
        assert client.patch("/api/v1/journey",json={"field":"reflections","value":{"build-a-tool":"I liked prototyping."}}).status_code==200
        assert client.patch("/api/v1/journey",json={"field":"comparison","value":["software-developer"]}).status_code==200
        assert client.get("/api/v1/journey").json()["profile"]["interests"]==["Technology"]
        assert client.post("/api/v1/auth/logout").status_code==204
        assert client.get("/api/v1/journey").status_code==401
        assert client.post("/api/v1/auth/login",json=credentials).status_code==200
        stored=client.get("/api/v1/journey").json()
        assert stored["profile"]==profile
        assert stored["selectedCareerId"]=="software-developer"
        assert stored["reflections"]["build-a-tool"]=="I liked prototyping."
        assert stored["comparison"]==["software-developer"]

def test_account_isolation_and_bad_login():
    with TestClient(app) as client:
        credentials=new_user(client)
        assert client.patch("/api/v1/journey",json={"field":"reflections","value":{"activity":"private"}}).status_code==200
        assert client.post("/api/v1/auth/login",json={**credentials,"password":"incorrect_pass_2026"}).status_code==401
        client.post("/api/v1/auth/logout")
        new_user(client)
        assert client.get("/api/v1/journey").json()["reflections"]=={}
        assert client.patch("/api/v1/journey",json={"field":"comparison","value":["a","b","c","d"]}).status_code==422
        assert client.patch("/api/v1/journey",json={"field":"chatHistory","value":[{"role":"system","content":"bad"}]}).status_code==422

def test_same_origin_and_unauthorized_mutation():
    with TestClient(app) as client:
        new_user(client)
        blocked=client.patch("/api/v1/journey",headers={"Origin":"https://other.example"},json={"field":"profile","value":None})
        assert blocked.status_code==403
        assert client.get("/api/v1/journey").status_code==200
        client.post("/api/v1/auth/logout")
        assert client.patch("/api/v1/journey",json={"field":"selectedCareerId","value":"software-developer"}).status_code==401


def test_auth_works_from_vite_fallback_port():
    with TestClient(app) as client:
        from uuid import uuid4
        credentials={"username":"vite_"+uuid4().hex[:12],"password":"correct_horse_2026"}
        origin="http://localhost:5174"
        response=client.post("/api/v1/auth/register",json=credentials,headers={"Origin":origin})
        assert response.status_code == 201, response.text
        assert client.get("/api/v1/auth/me").status_code == 200
        saved=client.patch("/api/v1/journey",headers={"Origin":origin},json={"field":"selectedCareerId","value":"example-career"})
        assert saved.status_code == 200, saved.text
        assert client.post("/api/v1/auth/logout",headers={"Origin":origin}).status_code == 204
        assert client.post("/api/v1/auth/login",json=credentials,headers={"Origin":origin}).status_code == 200
