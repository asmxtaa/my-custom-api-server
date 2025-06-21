from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app


client = TestClient(app)

def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
