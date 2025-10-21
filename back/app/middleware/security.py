from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


class SecurityMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, api_key_header_name: str, expected_api_key: str, allowed_origins: list[str]):
        super().__init__(app)
        self.api_key_header_name = api_key_header_name
        self.expected_api_key = expected_api_key
        self.allowed_origins = set(allowed_origins or [])

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # API Key validation
        api_key = request.headers.get(self.api_key_header_name)
        if not api_key or api_key != self.expected_api_key:
            return JSONResponse({"detail": "Unauthorized"}, status_code=401)

        # Origin/Referer validation (skip if none configured)
        if self.allowed_origins:
            origin = request.headers.get("origin") or request.headers.get("Origin")
            referer = request.headers.get("referer") or request.headers.get("Referer")

            # Normalize by stripping trailing slashes
            def normalize(value: str | None) -> str | None:
                if not value:
                    return None
                return value.rstrip("/")

            origin = normalize(origin)
            referer = normalize(referer)
            allowed = {o.rstrip("/") for o in self.allowed_origins}

            if origin is None and referer is None:
                return JSONResponse({"detail": "Forbidden"}, status_code=403)

            if origin and origin in allowed:
                return await call_next(request)
            if referer and referer in allowed:
                return await call_next(request)

            return JSONResponse({"detail": "Forbidden"}, status_code=403)

        return await call_next(request)



