import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_returns_message(client):
    response = client.get('/')
    data = response.get_json()
    assert 'message' in data

def test_health_returns_200(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_returns_healthy_status(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info_returns_200(client):
    response = client.get('/info')
    assert response.status_code == 200