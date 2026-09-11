import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_homepage_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "LinguaBridge AI" in response.text

def test_get_languages_endpoint():
    response = client.get("/api/languages")
    assert response.status_code == 200
    data = response.json()
    assert "languages" in data
    assert "ne" in data["languages"]
    assert "bn" in data["languages"]
    assert "my" in data["languages"]
    assert "en" in data["languages"]
    assert "hi" in data["languages"]
    assert "as" in data["languages"]
    assert "mni" not in data["languages"]

def test_translate_endpoint():
    payload = {
        "text": "नमस्ते",
        "source_lang": "ne",
        "target_lang": "en"
    }
    response = client.post("/api/translate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert "romanized_text" in data

def test_romanize_endpoint():
    payload = {
        "text": "तपाईंलाई कस्तो छ?",
        "lang": "ne"
    }
    response = client.post("/api/romanize", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["romanized"] == "Tapainlai kasto cha?"
