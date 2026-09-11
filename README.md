# LinguaBridge AI — Multilingual Voice & Text Translator

**LinguaBridge AI** is a modern, attractive, beginner-friendly multilingual translator web application built using **Python (FastAPI)**, HTML5, CSS3, and JavaScript.

It enables real-time interconvertible text translation, Romanization (pronunciation transliteration into Latin script), speech-to-text (STT), text-to-speech (TTS), speech-to-speech workflow, dual-person conversation mode, and translation history across 5 primary Asian and global languages:

- 🇳🇵 **Nepali** (`ne`)
- 🇧🇩 **Bengali** (`bn`)
- 🇮🇳 **Manipuri / Meitei** (`mni`)
- 🇲🇲 **Burmese** (`my`)
- 🇬🇧 **English** (`en`)

Every single language is **interconvertible with every other language** in both directions (20 direct pairs)!

---

## 🌟 Key Features

1. **Text Translation**: Fast bidirectional text translation with language swap, character count, copy, and clear controls.
2. **Romanization Engine**: Automatic transliteration of native non-Latin scripts (Devanagari, Bengali script, Meitei Mayek, Myanmar script) into Latin alphabet pronunciations.
3. **Cartoon Mascot Animated Microphone**: Interactive playful Shin-chan inspired cartoon mascot ("Bridgey") that reacts to voice input with glowing audio visualizers, speech bubbles, recording timers, and live waveforms.
4. **Speech-to-Text (STT)**: Browser Web Speech API with server-side audio upload fallback.
5. **Text-to-Speech (TTS)**: Web Speech Synthesis + server-side `gTTS` audio stream player with play, pause, stop, and speed controls.
6. **Speech-to-Speech Flow**: Speak in source language → Transcribe → Translate → Romanize → Auto-speak in target language.
7. **Conversation Mode**: Dual-person turn-taking interface (Person A vs Person B) with real-time speech translation bubbles.
8. **Translation History**: LocalStorage history persistence with instant search, audio replay, single item removal, and bulk clear.

---

## 🏗️ Architecture & Project Structure

```
linguabridge/
├── app/
│   ├── main.py                  # FastAPI application entrypoint & template rendering
│   ├── config.py                # Environment variables & language metadata configuration
│   ├── routes/
│   │   ├── translate.py         # REST endpoints for translation & Romanization
│   │   ├── speech.py            # REST endpoints for TTS audio generation & STT
│   │   └── history.py           # REST endpoints for history stats
│   ├── services/
│   │   ├── translator.py        # Multi-engine translation pipeline (Google, MyMemory, Lingva)
│   │   ├── romanizer.py         # Devanagari, Bengali, Meitei & Burmese script transliterator
│   │   ├── text_to_speech.py    # Server-side gTTS audio generator with caching
│   │   └── speech_to_text.py    # SpeechRecognition processor for audio clips
│   ├── templates/
│   │   └── index.html           # Modern single-page web app template
│   └── static/
│       ├── css/
│       │   ├── main.css         # Theme design system, variables, typography
│       │   ├── components.css   # Cards, selects, buttons, conversation chat bubbles
│       │   └── cartoon_mic.css  # Cartoon mascot "Bridgey", mic glow, visualizer CSS
│       └── js/
│           ├── app.js           # Core state controller & toast alerts
│           ├── translator.js    # Translation studio logic & auto-translate
│           ├── cartoon_mic.js   # Cartoon mascot animation engine & audio canvas
│           ├── speech.js        # Web Speech API (STT & TTS audio controls)
│           ├── conversation.js  # Dual-person conversation mode manager
│           └── history.js       # LocalStorage translation history manager
├── tests/
│   ├── test_translator.py       # Unit tests for translation engine
│   ├── test_romanizer.py        # Unit tests for Romanization engine
│   └── test_api.py              # Unit tests for FastAPI REST endpoints
├── .env.example
├── .env
├── requirements.txt
├── README.md
└── run.py
```

---

## 🛠️ Installation & Setup Guide

### 1. Clone / Navigate to Directory
```bash
cd linguabridge
```

### 2. Create and Activate Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Web Application

To launch the FastAPI dev server:
```bash
python3 run.py
```
Or using uvicorn directly:
```bash
uvicorn app.main:app --reload --port 8000
```

Open your browser at: **`http://localhost:8000`**

---

## 🧪 Running Automated Tests

Run the test suite with `pytest`:
```bash
pytest tests/
```

---

## 🎙️ Microphone & Speech Permissions
When using Speech-to-Text or Speech-to-Speech for the first time, your browser will prompt for microphone permissions. Ensure you select **Allow**.
