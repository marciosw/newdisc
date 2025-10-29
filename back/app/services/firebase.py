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

    try:
        # Initialize Firebase with credentials from settings
        cred = None
        
        # Try to use credentials from settings (environment variables)
        if settings.firebase_credentials_json:
            print("Using inline JSON credentials")
            # Use inline JSON credentials
            cred = credentials.Certificate(settings.firebase_credentials_json)
        elif settings.firebase_credentials_path:
            print(f"Using file path credentials: {settings.firebase_credentials_path}")
            # Use file path credentials
            cred = credentials.Certificate(settings.firebase_credentials_path)
        else:
            print("Using Application Default Credentials (ADC)")
            print("WARNING: This may cause permission issues if ADC doesn't have proper Firestore access")
            # Fall back to Application Default Credentials (ADC)
            # This works in production environments like Google Cloud Run
            cred = credentials.ApplicationDefault()

        _app = firebase_admin.initialize_app(cred, {
            "projectId": settings.firebase_project_id,
        })
        return _app
    except Exception as e:
        print(f"Firebase initialization failed: {e}")
        print("Continuing without Firebase - some endpoints may not work")
        # Return a dummy app to prevent crashes
        return None


def get_firestore_client() -> firestore.Client:
    app = initialize_firebase_if_needed()
    if app is None:
        raise Exception("Firebase not initialized - check credentials and project ID")
    return firestore.client()


def get_firebase_auth_info() -> dict:
    """
    Get detailed information about the Firebase authentication account being used.
    Returns a dictionary with authentication details.
    """
    try:
        app = initialize_firebase_if_needed()
        if app is None:
            return {"error": "Firebase not initialized - check credentials and project ID"}
        db = firestore.client()
        settings = get_settings()
        
        auth_info = {
            "firebase_app": {
                "name": app.name,
                "project_id": app.project_id,
                "options": dict(app.options) if hasattr(app, 'options') else None
            },
            "firestore_client": {
                "project": db.project if hasattr(db, 'project') else None,
                "client_type": str(type(db))
            }
        }
        
        # Add service account details if available
        if settings.firebase_credentials_json:
            creds = settings.firebase_credentials_json
            auth_info["service_account"] = {
                "client_email": creds.get('client_email'),
                "project_id": creds.get('project_id'),
                "client_id": creds.get('client_id'),
                "private_key_id": creds.get('private_key_id'),
                "type": creds.get('type'),
                "auth_uri": creds.get('auth_uri'),
                "token_uri": creds.get('token_uri')
            }
        else:
            auth_info["service_account"] = {
                "client_email": "Using Application Default Credentials (ADC)",
                "project_id": "Using Application Default Credentials (ADC)",
                "type": "adc"
            }
            
        # Add configuration details
        auth_info["configuration"] = {
            "firebase_project_id": settings.firebase_project_id,
            "credentials_source": "file_path" if settings.firebase_credentials_path else "inline_json" if settings.firebase_credentials_json else "application_default"
        }
        
        return auth_info
        
    except Exception as e:
        return {"error": f"Failed to get Firebase auth info: {str(e)}"}


