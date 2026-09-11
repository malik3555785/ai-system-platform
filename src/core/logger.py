"""Logging configuration"""

import logging
import logging.handlers
from pathlib import Path
from pythonjsonlogger import jsonlogger
from src.config.settings import settings


def setup_logging() -> logging.Logger:
    """Setup logging configuration"""
    
    # Create logs directory
    log_dir = Path(settings.LOG_FILE).parent
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger("ai_system")
    logger.setLevel(getattr(logging, settings.LOG_LEVEL))
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=settings.LOG_MAX_BYTES,
        backupCount=settings.LOG_BACKUP_COUNT
    )
    
    # JSON formatter
    formatter = jsonlogger.JsonFormatter()
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    return logger
