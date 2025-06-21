import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from database import get_database

client = TestClient(app)

@pytest.fixture
def test_db():
    # Setup test DB connection
    db = get_database(test=True)  # You must implement test mode in your DB code
    yield db
    # Teardown test DB (clean collections etc.)

def test_create_book_api(test_db):
    response = client.post("/books", json={
        "title": "Integration Test Book",
        "author": "Tester",
        "published_year": 2025,
        "genre": "Test"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Integration Test Book"
