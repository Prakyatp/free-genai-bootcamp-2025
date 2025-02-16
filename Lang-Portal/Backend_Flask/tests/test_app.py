import pytest
from app import create_app

@pytest.fixture
def app():
    """Create a test app instance"""
    app = create_app()
    return app

@pytest.fixture
def client(app):
    """Create a test client"""
    return app.test_client()

def test_home_page(client):
    """Test the home page route"""
    response = client.get('/')
    assert response.status_code == 200

def test_api_words(client):
    """Test the words API endpoint"""
    response = client.get('/api/words')
    assert response.status_code == 200

def test_api_groups(client):
    """Test the groups API endpoint"""
    response = client.get('/api/groups')
    assert response.status_code == 200