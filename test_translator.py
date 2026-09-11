import pytest
from app.services.translator import translator_service

@pytest.mark.asyncio
async def test_identity_translation():
    res = await translator_service.translate("Namaste", "ne", "ne")
    assert res["translated_text"] == "Namaste"
    assert res["engine_used"] == "identity"

@pytest.mark.asyncio
async def test_offline_dictionary_translation():
    res = await translator_service.translate("तपाईंलाई कस्तो छ?", "ne", "en")
    assert res["translated_text"] == "How are you?"
    assert res["romanized_text"] == "How are you?"

@pytest.mark.asyncio
async def test_hindi_to_english():
    res = await translator_service.translate("आप कैसे हैं?", "hi", "en")
    assert res["translated_text"] == "How are you?"

@pytest.mark.asyncio
async def test_assamese_to_english():
    res = await translator_service.translate("আপুনি কেনেকৈ আছে?", "as", "en")
    assert res["translated_text"] == "How are you?"

@pytest.mark.asyncio
async def test_nepali_to_burmese_interconvertible():
    res = await translator_service.translate("तपाईंलाई कस्तो छ?", "ne", "my")
    assert res["translated_text"] != ""
    assert res["target_lang"] == "my"

@pytest.mark.asyncio
async def test_hindi_to_assamese_interconvertible():
    res = await translator_service.translate("नमस्ते", "hi", "as")
    assert res["translated_text"] != ""
    assert res["target_lang"] == "as"

@pytest.mark.asyncio
async def test_empty_translation():
    res = await translator_service.translate("", "ne", "en")
    assert res["translated_text"] == ""
