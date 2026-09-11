import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.routes.translate import router as translate_router
from app.routes.speech import router as speech_router
from app.routes.history import router as history_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title=settings.APP_NAME,
    description="Multilingual Voice & Text Translator for Nepali, Bengali, Manipuri, Burmese, and English.",
    version="1.0.0"
)

# Enable CORS for frontend freedom
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static directory
static_dir = BASE_DIR / "static"
static_dir.mkdir(parents=True, exist_ok=True)
(static_dir / "audio").mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Templates Setup
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Include API Routers
app.include_router(translate_router)
app.include_router(speech_router)
app.include_router(history_router)

@app.get("/")
async def render_homepage(request: Request):
    """
    Renders the main single page web application.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.APP_NAME,
            "languages": settings.SUPPORTED_LANGUAGES,
            "default_source": settings.DEFAULT_SOURCE_LANG,
            "default_target": settings.DEFAULT_TARGET_LANG
        }
    )

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "An unexpected error occurred. Please check your internet connection and try again.",
            "detail": str(exc) if settings.ENVIRONMENT == "development" else None
        }
    )
