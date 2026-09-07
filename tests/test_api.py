from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Task Management API is running"


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Test User",
            "email": "testuser123@gmail.com"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "testuser123@gmail.com"


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing task API",
            "user_id": 1
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["status"] == "pending"