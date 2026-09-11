"""Application settings and configuration"""

import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    API_HOST: str = Field(default="0.0.0.0", env="API_HOST")
    API_PORT: int = Field(default=8000, env="API_PORT")
    DEBUG: bool = Field(default=False, env="API_DEBUG")
    LOG_LEVEL: str = Field(default="INFO", env="API_LOG_LEVEL")
    
    # External API Configuration
    EXTERNAL_API_BASE_URL: str = Field(default="https://apis.davidcyril.name.ng", env="EXTERNAL_API_BASE_URL")
    EXTERNAL_API_TIMEOUT: int = Field(default=30, env="EXTERNAL_API_TIMEOUT")
    EXTERNAL_API_RETRY_ATTEMPTS: int = Field(default=3, env="EXTERNAL_API_RETRY_ATTEMPTS")
    
    # Model Configuration
    GPT5_API_KEY: str = Field(default="", env="GPT5_API_KEY")
    CLAUDE_API_KEY: str = Field(default="", env="CLAUDE_API_KEY")
    DEFAULT_MODEL: str = Field(default="gpt-4", env="DEFAULT_MODEL")
    MODEL_TIMEOUT: int = Field(default=30, env="MODEL_TIMEOUT")
    
    # Database Configuration
    DATABASE_URL: str = Field(default="sqlite:///./data/ai_system.db", env="DATABASE_URL")
    DATABASE_POOL_SIZE: int = Field(default=10, env="DATABASE_POOL_SIZE")
    DATABASE_ECHO: bool = Field(default=False, env="DATABASE_ECHO")
    
    # Cache Configuration
    REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    CACHE_TTL: int = Field(default=3600, env="CACHE_TTL")
    
    # Authentication
    AUTH_SECRET_KEY: str = Field(default="your_super_secret_key", env="AUTH_SECRET_KEY")
    AUTH_ALGORITHM: str = Field(default="HS256", env="AUTH_ALGORITHM")
    AUTH_EXPIRATION_HOURS: int = Field(default=24, env="AUTH_EXPIRATION_HOURS")
    JWT_SECRET_KEY: str = Field(default="your_jwt_secret_key", env="JWT_SECRET_KEY")
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = Field(default=True, env="RATE_LIMIT_ENABLED")
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = Field(default=60, env="RATE_LIMIT_REQUESTS_PER_MINUTE")
    
    # Logging
    LOG_FILE: str = Field(default="logs/ai_system.log", env="LOG_FILE")
    LOG_MAX_BYTES: int = Field(default=10485760, env="LOG_MAX_BYTES")
    LOG_BACKUP_COUNT: int = Field(default=5, env="LOG_BACKUP_COUNT")
    
    # Monitoring
    MONITORING_ENABLED: bool = Field(default=True, env="MONITORING_ENABLED")
    MONITORING_PROMETHEUS_PORT: int = Field(default=9090, env="MONITORING_PROMETHEUS_PORT")
    
    # System
    SYSTEM_NAME: str = Field(default="AI-System-Platform", env="SYSTEM_NAME")
    SYSTEM_VERSION: str = Field(default="2.0.0", env="SYSTEM_VERSION")
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    
    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:3000"],
        env="CORS_ORIGINS"
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
