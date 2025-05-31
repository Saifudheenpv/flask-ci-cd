import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """Test the main endpoint returns correct HTML response."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, DevOps World!' in response.data
    assert b'<!DOCTYPE html>' in response.data


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'Healthy' in response.data
    assert b'<!DOCTYPE html>' in response.data


def test_api_health_check(client):
    """Test the API health check endpoint returns JSON."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert data['version'] == '1.0.0'


def test_404_handler(client):
    """Test 404 error handler."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Resource not found' in response.data
    assert b'<!DOCTYPE html>' in response.data
