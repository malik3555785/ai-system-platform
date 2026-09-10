"""
Cache Configuration and Management
"""

import logging
import json
from typing import Any, Optional

import redis.asyncio as redis
from redis.asyncio import Redis

from src.config.settings import get_settings

logger = logging.getLogger("ai_system")

# Global cache instance
cache_instance: Optional[Redis] = None


async def init_cache() -> None:
    """
    Initialize cache connection
    """
    global cache_instance
    
    settings = get_settings()
    
    try:
        cache_instance = await redis.from_url(settings.REDIS_URL, decode_responses=True)
        await cache_instance.ping()
        logger.info("Cache initialized successfully")
    except Exception as e:
        logger.warning(f"Cache initialization failed: {e}. Operating without cache.")
        cache_instance = None


async def get_cache() -> Optional[Redis]:
    """
    Get cache instance
    """
    return cache_instance


async def cache_set(key: str, value: Any, ttl: Optional[int] = None) -> bool:
    """
    Set value in cache
    """
    if cache_instance is None:
        return False
    
    try:
        settings = get_settings()
        ttl = ttl or settings.CACHE_TTL
        await cache_instance.setex(key, ttl, json.dumps(value, default=str))
        return True
    except Exception as e:
        logger.error(f"Cache set error: {e}")
        return False


async def cache_get(key: str) -> Optional[Any]:
    """
    Get value from cache
    """
    if cache_instance is None:
        return None
    
    try:
        value = await cache_instance.get(key)
        if value:
            return json.loads(value)
        return None
    except Exception as e:
        logger.error(f"Cache get error: {e}")
        return None


async def cache_delete(key: str) -> bool:
    """
    Delete key from cache
    """
    if cache_instance is None:
        return False
    
    try:
        await cache_instance.delete(key)
        return True
    except Exception as e:
        logger.error(f"Cache delete error: {e}")
        return False


async def close_cache() -> None:
    """
    Close cache connection
    """
    global cache_instance
    if cache_instance:
        await cache_instance.close()
        logger.info("Cache connection closed")
