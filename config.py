import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "LinguaBridge AI")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PORT: int = int(os.getenv("PORT", 8000))
    HOST: str = os.getenv("HOST", "0.0.0.0")
    
    DEFAULT_SOURCE_LANG: str = os.getenv("DEFAULT_SOURCE_LANG", "ne")
    DEFAULT_TARGET_LANG: str = os.getenv("DEFAULT_TARGET_LANG", "en")
    MAX_TEXT_LENGTH: int = int(os.getenv("MAX_TEXT_LENGTH", 5000))
    
    # Supported Languages metadata
    SUPPORTED_LANGUAGES = {
        "en": {
            "name": "English",
            "native_name": "English",
            "flag": "🇬🇧",
            "speech_code": "en-US",
            "tts_code": "en",
            "char_img": "/static/images/characters/en.png",
            "char_num": "1",
            "char_desc": "English Gentleman"
        },
        "my": {
            "name": "Burmese",
            "native_name": "မြန်မာစာ",
            "flag": "🇲🇲",
            "speech_code": "my-MM",
            "tts_code": "my",
            "char_img": "/static/images/characters/my.png",
            "char_num": "2",
            "char_desc": "Burmese Maiden"
        },
        "ne": {
            "name": "Nepali",
            "native_name": "नेपाली",
            "flag": "🇳🇵",
            "speech_code": "ne-NP",
            "tts_code": "ne",
            "char_img": "/static/images/characters/ne.png",
            "char_num": "3",
            "char_desc": "Nepali Traditional"
        },
        "as": {
            "name": "Assamese",
            "native_name": "অসমীয়া",
            "flag": "🇮🇳",
            "speech_code": "as-IN",
            "tts_code": "bn",  # Assamese script audio phonetics fallback
            "char_img": "/static/images/characters/as.png",
            "char_num": "4",
            "char_desc": "Assamese Maiden"
        },
        "bn": {
            "name": "Bengali",
            "native_name": "বাংলা",
            "flag": "🇧🇩",
            "speech_code": "bn-BD",
            "tts_code": "bn",
            "char_img": "/static/images/characters/bn.png",
            "char_num": "5",
            "char_desc": "Bengali Maiden"
        },
        "hi": {
            "name": "Hindi",
            "native_name": "हिन्दी",
            "flag": "🇮🇳",
            "speech_code": "hi-IN",
            "tts_code": "hi",
            "char_img": "/static/images/characters/hi.png",
            "char_num": "6",
            "char_desc": "Hindi Attire"
        }
    }

settings = Settings()
