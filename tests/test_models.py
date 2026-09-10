"""
Model Management Tests
"""

import pytest
from fastapi.testclient import TestClient

from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_list_models(client):
    response = client.get("/api/models/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]


def test_get_model(client):
    response = client.get("/api/models/gpt-5")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "gpt-5"
    assert "capabilities" in data
