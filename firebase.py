import os
import logging
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from pathlib import Path

logger = logging.getLogger("linguabridge.firebase")

_db = None


def _initialize_firebase() -> None:
    """Initialize Firebase Admin SDK (runs once at startup)."""
    if firebase_admin._apps:
        return

    service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY", "")

    try:
        if service_account_path and Path(service_account_path).exists():
            cred = credentials.Certificate(service_account_path)
            logger.info(f"🔥 Firebase: Using service account from {service_account_path}")
        else:
            cred = credentials.ApplicationDefault()
            logger.info("🔥 Firebase: Using Application Default Credentials")

        firebase_admin.initialize_app(cred, {
            "projectId": os.getenv("FIREBASE_PROJECT_ID", "language-translator-fda96"),
        })
    except Exception as e:
        logger.warning(f"Firebase Admin init skipped/failed: {e}")


def get_db():
    """
    Returns the Firestore async client, initialising Firebase if needed.
    Returns None if Firestore is not accessible.
    """
    global _db
    if _db is None:
        try:
            _initialize_firebase()
            service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY", "")
            project_id = os.getenv("FIREBASE_PROJECT_ID", "language-translator-fda96")
            if service_account_path and Path(service_account_path).exists():
                _db = firestore.AsyncClient.from_service_account_json(service_account_path)
            else:
                _db = firestore.AsyncClient(project=project_id)
        except Exception as e:
            logger.warning(f"Firestore AsyncClient unavailable: {e}")
            return None
    return _db

