#!/usr/bin/env python3
"""
AI System Platform - Main Entry Point
"""

import asyncio
import logging
import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

from src.api.app import create_app
from src.config.settings import Settings
from src.core.logger import setup_logging
from src.core.database import init_database
from src.core.cache import init_cache

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logging()


async def initialize_system():
    """
    Initialize all system components
    """
    logger.info("Initializing AI System Platform...")
    
    try:
        # Initialize database
        logger.info("Initializing database...")
        await init_database()
        logger.info("✓ Database initialized")
        
        # Initialize cache
        logger.info("Initializing cache...")
        await init_cache()
        logger.info("✓ Cache initialized")
        
        logger.info("✓ System initialization complete")
        return True
    except Exception as e:
        logger.error(f"✗ System initialization failed: {e}", exc_info=True)
        return False


def main():
    """
    Main entry point
    """
    settings = Settings()
    
    logger.info(f"Starting {settings.SYSTEM_NAME} v{settings.SYSTEM_VERSION}")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    
    # Initialize system
    try:
        init_success = asyncio.run(initialize_system())
        if not init_success:
            logger.error("Failed to initialize system components")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Initialization error: {e}", exc_info=True)
        sys.exit(1)
    
    # Create FastAPI application
    app = create_app()
    
    # Run server
    logger.info(f"Starting server on {settings.API_HOST}:{settings.API_PORT}")
    logger.info(f"API Documentation: http://{settings.API_HOST}:{settings.API_PORT}/docs")
    
    try:
        uvicorn.run(
            app,
            host=settings.API_HOST,
            port=settings.API_PORT,
            debug=settings.DEBUG,
            log_level=settings.LOG_LEVEL.lower(),
        )
    except KeyboardInterrupt:
        logger.info("Shutdown signal received")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
