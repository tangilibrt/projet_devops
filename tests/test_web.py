import pytest
from unittest.mock import patch
from web_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_greet_french_day_returns_200(client):
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 10
        response = client.get("/greet/fr")
        assert response.status_code == 200


def test_greet_french_day_message(client):
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 10
        data = client.get("/greet/fr").get_json()
        assert data["message"] == "Bonjour"


def test_greet_french_evening_message(client):
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 20
        data = client.get("/greet/fr").get_json()
        assert data["message"] == "Bonsoir"


def test_greet_unknown_lang_returns_404(client):
    response = client.get("/greet/xx")
    assert response.status_code == 404
