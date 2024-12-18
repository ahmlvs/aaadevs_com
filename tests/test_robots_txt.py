from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert "User-agent: *" in response.text
    assert "Disallow: /404" in response.text
    assert "Allow: /" in response.text
