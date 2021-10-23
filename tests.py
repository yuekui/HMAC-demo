from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_generate_token(monkeypatch):
    monkeypatch.setenv("HMAC_KEY", "TEST-KEY")
    response = client.post("/generate-token", json={"id": "test"})
    assert response.status_code == 200, response.text
    assert response.json() == {
        "id": "test",
        "signature": "a81afdf31173556887ab54cbb5ef7e8dc6d2d47f462ef43ad599225394616ef9",
    }
