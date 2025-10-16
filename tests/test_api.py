from fastapi.testclient import TestClient
from src.predict_service import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body.get("status") == "ok"
    assert "model_version" in body
