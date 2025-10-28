from functools import lru_cache
from pydantic import BaseModel
import os
import json
from dotenv import load_dotenv
from typing import Optional
import pathlib
import base64
import binascii
import warnings

# Load environment variables from a .env file if present
load_dotenv()


class Settings(BaseModel):
    api_key: str
    allowed_origins: list[str]
    firebase_project_id: str | None = None
    firebase_credentials_json: dict | None = None
    firebase_credentials_path: str | None = None


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    api_key = os.getenv("API_KEY", "")
    allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "")
    allowed_origins = [o.strip() for o in allowed_origins_env.split(",") if o.strip()]

    firebase_project_id = os.getenv("FIREBASE_PROJECT_ID", "ouzaz-ac5bd")  # Default to your project ID
    firebase_credentials_inline = os.getenv("FIREBASE_CREDENTIALS_JSON")
    firebase_credentials_path_env = os.getenv("FIREBASE_CREDENTIALS_PATH")
    firebase_credentials_json = None
    firebase_credentials_path: Optional[str] = None

    # If a path env is provided, prefer it
    if firebase_credentials_path_env:
        path_obj = pathlib.Path(firebase_credentials_path_env)
        if path_obj.is_file():
            try:
                firebase_credentials_json = json.loads(path_obj.read_text())
                firebase_credentials_path = str(path_obj)
            except json.JSONDecodeError:
                warnings.warn("FIREBASE_CREDENTIALS_PATH found but file is not valid JSON; falling back to Application Default credentials.")
        else:
            warnings.warn("FIREBASE_CREDENTIALS_PATH is set but not a valid file; falling back to Application Default credentials.")

    # Otherwise try inline JSON
    elif firebase_credentials_inline:
        raw = firebase_credentials_inline.strip()
        # If the whole value is quoted, remove one pair of matching quotes
        if (raw.startswith("\"") and raw.endswith("\"")) or (raw.startswith("'") and raw.endswith("'")):
            raw = raw[1:-1]
        # Replace common escaped newlines (from .env) before parsing
        normalized = raw.replace("\\n", "\n")
        try:
            firebase_credentials_json = json.loads(normalized)
        except json.JSONDecodeError:
            # Try treating as a file path
            candidate = pathlib.Path(raw)
            if candidate.is_file():
                try:
                    firebase_credentials_json = json.loads(candidate.read_text())
                    firebase_credentials_path = str(candidate)
                except json.JSONDecodeError:
                    warnings.warn("FIREBASE_CREDENTIALS_JSON path provided but file is not valid JSON; falling back to Application Default credentials.")
            else:
                # Try base64-decoded JSON
                try:
                    decoded = base64.b64decode(raw)
                    firebase_credentials_json = json.loads(decoded)
                except (binascii.Error, json.JSONDecodeError, ValueError):
                    warnings.warn("FIREBASE_CREDENTIALS_JSON not valid JSON/path/base64; falling back to Application Default credentials.")

    # Fallback: Try to use the service-account.json file in the project root
    if not firebase_credentials_json and not firebase_credentials_path:
        service_account_paths = [
            pathlib.Path("service-account.json"),
            pathlib.Path("app/service-account.json"),
            pathlib.Path("/Users/marciomacedo/Documents/dev/github/newdisc/back/service-account.json"),
            pathlib.Path("/Users/marciomacedo/Documents/dev/github/newdisc/back/app/service-account.json")
        ]
        
        for path in service_account_paths:
            if path.is_file():
                try:
                    firebase_credentials_json = json.loads(path.read_text())
                    firebase_credentials_path = str(path)
                    print(f"Using service account file: {path}")
                    break
                except json.JSONDecodeError:
                    continue

    if not api_key:
        raise ValueError("API_KEY environment variable must be set")

    return Settings(
        api_key=api_key,
        allowed_origins=allowed_origins,
        firebase_project_id=firebase_project_id,
        firebase_credentials_json=firebase_credentials_json,
        firebase_credentials_path=firebase_credentials_path,
    )


