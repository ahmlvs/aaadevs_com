from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_sitemap_xml():
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/xml")
    assert "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" in response.text
    assert "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" in response.text
    assert "<loc>https://aaadevs.com/</loc>" in response.text
