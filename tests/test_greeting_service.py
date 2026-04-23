from unittest.mock import patch
from services.greeting_service import get_greeting


def test_daytime_french():
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 10
        assert get_greeting("fr") == "Bonjour"


def test_evening_french():
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 20
        assert get_greeting("fr") == "Bonsoir"


def test_english_morning():
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 9
        assert get_greeting("en") == "Good morning"


def test_english_evening():
    with patch("services.greeting_service.datetime") as mock_dt:
        mock_dt.now.return_value.hour = 19
        assert get_greeting("en") == "Good evening"


def test_unknown_language_returns_none():
    assert get_greeting("xx") is None
