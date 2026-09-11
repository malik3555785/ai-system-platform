"""Model endpoint tests"""

import pytest
from fastapi.testclient import TestClient
from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_list_models(client):
    """Test list models endpoint"""
    response = client.get("/api/v1/models/list")
    assert response.status_code == 200
    data = response.json()
    assert "models" in data
    assert "count" in data
    assert len(data["models"]) > 0


def test_get_model(client):
    """Test get specific model endpoint"""
    response = client.get("/api/v1/models/gpt-4")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "gpt-4"
    assert data["provider"] == "OpenAI"


def test_get_nonexistent_model(client):
    """Test get nonexistent model returns 404"""
    response = client.get("/api/v1/models/nonexistent-model")
    assert response.status_code == 404
