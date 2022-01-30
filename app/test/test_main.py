from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_usa_data():
    response = client.get("/get_usa_data")
    assert response.status_code == 403
    # assert type(response.json()) == 'Dictionary'


def test_login_bad_token():
    response = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": "string",
            "password": "string"
        },
    )
    assert response.status_code == 404


def test_login_and_get_usa_data_with_valid_token():
    login_response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "admin"
        },
    )
    assert login_response.status_code == 200
    get_usa_data_response = client.get(
        "/get_usa_data", headers={"Authorization": f"Bearer {login_response.json()['token']}"})
    assert get_usa_data_response.status_code == 200
