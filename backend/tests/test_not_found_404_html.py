from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_custom_404_handler():
    response = client.get("/nonexistent-page")
    assert response.status_code == 404
    assert "text/html" in response.headers["content-type"]
    assert "404 - Page Not Found" in response.text
    assert "The page you are looking for does not exist." in response.text
