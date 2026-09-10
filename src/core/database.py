"""
Database Configuration and Connection Management
"""

import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

from src.config.settings import get_settings

logger = logging.getLogger("ai_system")

# Base class for models
Base = declarative_base()

# Global engine and session factory
engine: AsyncEngine = None
AsyncSessionLocal = None


async def init_database() -> None:
    """
    Initialize database connection
    """
    global engine, AsyncSessionLocal
    
    settings = get_settings()
    
    # Create async engine
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=settings.DATABASE_ECHO,
        pool_size=settings.DATABASE_POOL_SIZE,
        pool_pre_ping=True,
        poolclass=NullPool if "sqlite" in settings.DATABASE_URL else None,
    )
    
    # Create session factory
    AsyncSessionLocal = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    logger.info("Database initialized successfully")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Get database session
    """
    if AsyncSessionLocal is None:
        raise RuntimeError("Database not initialized")
    
    session = AsyncSessionLocal()
    try:
        yield session
    finally:
        await session.close()


async def close_database() -> None:
    """
    Close database connection
    """
    global engine
    if engine:
        await engine.dispose()
        logger.info("Database connection closed")
