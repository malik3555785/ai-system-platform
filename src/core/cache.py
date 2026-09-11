"""Cache management using Redis"""

import logging
import redis
import json
from typing import Any, Optional
from src.config.settings import settings

logger = logging.getLogger("ai_system")

redis_client: Optional[redis.Redis] = None


async def init_cache():
    """Initialize cache"""
    global redis_client
    logger.info("Initializing cache...")
    try:
        redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
        redis_client.ping()
        logger.info("Cache initialized successfully")
    except Exception as e:
        logger.warning(f"Cache initialization warning: {e}")
        redis_client = None


def get_cache():
    """Get cache instance"""
    return redis_client
