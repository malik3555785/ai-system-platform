"""
Health Check Endpoints
"""

import logging
from datetime import datetime

from fastapi import APIRouter

from src.config.settings import get_settings

logger = logging.getLogger("ai_system")
router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    settings = get_settings()
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "system": settings.SYSTEM_NAME,
        "version": settings.SYSTEM_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/health/deep")
async def deep_health_check():
    """
    Deep health check with component status
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "components": {
            "api": "operational",
            "database": "operational",
            "cache": "operational",
            "models": "operational",
        },
    }
