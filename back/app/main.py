from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .middleware.security import SecurityMiddleware
from .routers import health, v1


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title="NewDisc API", version="0.1.0")

    # CORS middleware - Allow requests from localhost:3000
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "https://localhost:3000", "https://newdisc.ouzaz.com.br", "https://ouzaz-ac5bd.web.app"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Security middleware - TEMPORARILY DISABLED
    # application.add_middleware(
    #     SecurityMiddleware,
    #     api_key_header_name="X-API-Key",
    #     expected_api_key=settings.api_key,
    #     allowed_origins=settings.allowed_origins,
    # )

    # Routers
    application.include_router(health.router, prefix="")
    application.include_router(v1.router, prefix="/v1")

    return application


app = create_app()


