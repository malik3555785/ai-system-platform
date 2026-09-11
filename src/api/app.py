"""FastAPI application factory"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.config.settings import settings
from src.api.routes import models, external_apis, chat, health


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    
    app = FastAPI(
        title=settings.SYSTEM_NAME,
        description="Comprehensive AI System Platform with Multi-Model Support",
        version=settings.SYSTEM_VERSION,
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(health.router, tags=["Health"])
    app.include_router(models.router, prefix="/api/v1/models", tags=["Models"])
    app.include_router(external_apis.router, prefix="/api/v1/external", tags=["External APIs"])
    app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
    
    @app.on_event("startup")
    async def startup():
        """Startup event"""
        pass
    
    @app.on_event("shutdown")
    async def shutdown():
        """Shutdown event"""
        pass
    
    return app
