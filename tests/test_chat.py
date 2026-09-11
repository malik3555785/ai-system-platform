"""Chat endpoint tests"""

import pytest
from fastapi.testclient import TestClient
from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_send_message(client):
    """Test sending chat message"""
    payload = {
        "content": "Hello, AI!",
        "model": "gpt-4"
    }
    response = client.post("/api/v1/chat/message", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["model"] == "gpt-4"
    assert "timestamp" in data


def test_get_chat_history(client):
    """Test getting chat history"""
    response = client.get("/api/v1/chat/history/test-session")
    assert response.status_code == 200
    data = response.json()
    assert data["session_id"] == "test-session"
    assert "messages" in data


def test_clear_chat_history(client):
    """Test clearing chat history"""
    response = client.delete("/api/v1/chat/clear/test-session")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "cleared"
