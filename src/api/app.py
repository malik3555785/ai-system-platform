"""
FastAPI Application Factory
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.config.settings import get_settings
from src.core.cache import close_cache
from src.core.database import close_database
from src.api.routes import health, models, chat, tools

logger = logging.getLogger("ai_system")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifecycle
    """
    # Startup
    logger.info("Application startup")
    yield
    # Shutdown
    logger.info("Application shutdown")
    await close_database()
    await close_cache()


def create_app() -> FastAPI:
    """
    Create and configure FastAPI application
    """
    settings = get_settings()
    
    app = FastAPI(
        title=settings.SYSTEM_NAME,
        version=settings.SYSTEM_VERSION,
        description="Comprehensive AI System Platform",
        lifespan=lifespan,
    )
    
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Trusted Host Middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"],
    )
    
    # Global exception handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "error_type": type(exc).__name__},
        )
    
    # Include routers
    app.include_router(health.router, tags=["Health"])
    app.include_router(models.router, prefix="/api/models", tags=["Models"])
    app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
    app.include_router(tools.router, prefix="/api/tools", tags=["Tools"])
    
    return app
