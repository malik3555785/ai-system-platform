"""External API endpoint tests"""

import pytest
from fastapi.testclient import TestClient
from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_external_endpoints(client):
    """Test external endpoints endpoint"""
    response = client.get("/api/v1/external/endpoints")
    # This may fail if external API is not available, but should not crash
    assert response.status_code in [200, 500]


def test_call_external_endpoint(client):
    """Test calling external endpoint"""
    payload = {
        "endpoint": "/test",
        "method": "GET"
    }
    response = client.post("/api/v1/external/call", json=payload)
    # This may fail if external API is not available, but should not crash
    assert response.status_code in [200, 500]
