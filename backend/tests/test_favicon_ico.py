from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_favicon_ico():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/x-icon"
    assert response.content  # Ensure the response has non-empty content
