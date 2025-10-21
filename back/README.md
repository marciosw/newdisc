## NewDisc API - FastAPI Base

This is a base FastAPI service prepared for calling external APIs and databases, exposing data to multiple sites. It includes:

- API key authentication and Referer/Origin validation middleware
- Firebase Admin SDK initialization
- Docker setup for Cloud Run deployment

### Quickstart (local)

1. Create and activate a virtual environment.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set environment variables (see Configuration below).
4. Run the server:

```
uvicorn app.main:app --reload
```

Open http://localhost:8000/health

### Configuration

Environment variables:

- API_KEY: Secret key required in `X-API-Key` header
- ALLOWED_ORIGINS: Comma-separated list of allowed origins or referers (exact match). Example: `https://example.com,https://www.example.com`
- FIREBASE_PROJECT_ID: Firebase project id
- FIREBASE_CREDENTIALS_JSON: (optional) Inline JSON for a service account key; if not provided, `GOOGLE_APPLICATION_CREDENTIALS` file path will be used by the SDK

### Deploy to Cloud Run

1. Build the image:

```
gcloud builds submit --tag gcr.io/ouzaz-ac5bd/newdiscapi
```

2. Deploy:

```
gcloud run deploy newdiscapi \
  --image gcr.io/ouzaz-ac5bd/newdiscapi \
  --region southamerica-east1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars API_KEY=your_api_key,ALLOWED_ORIGINS=https://example.com \
  --set-env-vars FIREBASE_PROJECT_ID=ouzaz-ac5bd
```

If using inline credentials, also set `FIREBASE_CREDENTIALS_JSON`.

Alternatively, you can use the provided `cloudrun.yaml`:

```
gcloud run services replace cloudrun.yaml --region REGION
```


Dados para o .env

API_KEY=your_api_key
ALLOWED_ORIGINS=https://example.com
FIREBASE_PROJECT_ID=your_project_id
Optionally FIREBASE_CREDENTIALS_JSON='{"type":"service_account",...}'

/Users/marciomacedo/Downloads/google-cloud-sdk/bin/