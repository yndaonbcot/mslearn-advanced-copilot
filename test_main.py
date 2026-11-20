from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_region_cities():
    response = client.get("/regions/France")
    assert response.status_code == 200
    assert response.json() == ["Paris"]


def test_unknown_region_is_not_found():
    response = client.get("/regions/france")
    assert response.status_code == 404
    assert response.json() == {"detail": "Region not found"}


def test_monthly_average_response():
    response = client.get("/countries/England/London/January")
    assert response.status_code == 200
    assert response.json() == {"high": 45, "low": 36}