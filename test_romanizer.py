import pytest
from app.services.romanizer import romanizer_service

def test_devanagari_nepali_romanization():
    text = "तपाईंलाई कस्तो छ?"
    res = romanizer_service.romanize(text, "ne")
    assert res == "Tapainlai kasto cha?"

def test_hindi_romanization():
    text = "आप कैसे हैं?"
    res = romanizer_service.romanize(text, "hi")
    assert res == "Aap kaise hain?"

def test_assamese_romanization():
    text = "আপুনি কেনেকৈ আছে?"
    res = romanizer_service.romanize(text, "as")
    assert res == "Apuni kenekoi ase?"

def test_bengali_romanization():
    text = "আপনি কেমন আছেন?"
    res = romanizer_service.romanize(text, "bn")
    assert "Apni" in res or "kemon" in res

def test_burmese_romanization():
    text = "မင်္ဂလာပါ"
    res = romanizer_service.romanize(text, "my")
    assert res == "Mingalarpar"

def test_english_romanization_passthrough():
    text = "Hello world"
    res = romanizer_service.romanize(text, "en")
    assert res == "Hello world"
