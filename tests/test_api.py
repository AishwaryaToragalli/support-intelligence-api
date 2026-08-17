from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200


def test_create_ticket():
    response = client.post(
        "/tickets",
        json={
            "title": "Database failure",
            "description": "The database is unavailable",
            "priority": "high",
        },
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Database failure"
