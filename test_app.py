from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "data" in data