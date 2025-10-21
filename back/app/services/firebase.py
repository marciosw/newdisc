from typing import Optional
import firebase_admin
from firebase_admin import credentials, firestore
from ..config import get_settings


_app: Optional[firebase_admin.App] = None


def initialize_firebase_if_needed() -> firebase_admin.App:
    global _app
    if _app is not None:
        return _app

    settings = get_settings()
    if firebase_admin._apps:
        _app = firebase_admin.get_app()
        return _app

    # Initialize Firebase with credentials from settings
    cred = None
    
    # Try to use credentials from settings (environment variables)
    if settings.firebase_credentials_json:
        # Use inline JSON credentials
        cred = credentials.Certificate(settings.firebase_credentials_json)
    elif settings.firebase_credentials_path:
        # Use file path credentials
        cred = credentials.Certificate(settings.firebase_credentials_path)
    else:
        # Fall back to Application Default Credentials (ADC)
        # This works in production environments like Google Cloud Run
        cred = credentials.ApplicationDefault()

    _app = firebase_admin.initialize_app(cred, {
        "projectId": settings.firebase_project_id,
    })
    return _app


def get_firestore_client() -> firestore.Client:
    initialize_firebase_if_needed()
    return firestore.client()


