from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "AAA Devs creates innovative Telegram and Discord applications designed to help your business build, scale, and thrive." in response.text
