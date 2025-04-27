from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timezone

client = TestClient(app)

def test_get_user_success():
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Knaz"

#def test_get_user_not_found():
#    response = client.get("/api/v1/users/999")
#    assert response.status_code == 404
#    assert response.json() == {"detail": "User not found"}

def test_response_format_json():
    response = client.get("/api/v1/users/1", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

def test_response_format_xml():
    response = client.get("/api/v1/users/1", headers={"Accept": "application/xml"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
