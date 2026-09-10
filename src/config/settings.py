"""
Application Settings and Configuration
"""

from typing import Literal
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field, validator


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    
    # API Configuration
    API_HOST: str = Field(default="0.0.0.0", description="API host address")
    API_PORT: int = Field(default=8000, description="API port")
    DEBUG: bool = Field(default=False, description="Debug mode")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    
    # System Configuration
    SYSTEM_NAME: str = Field(default="AI-System-Platform", description="System name")
    SYSTEM_VERSION: str = Field(default="1.0.0", description="System version")
    ENVIRONMENT: Literal["development", "staging", "production"] = Field(
        default="development", description="Environment"
    )
    
    # Model Configuration
    GPT5_API_KEY: str = Field(default="", description="GPT-5 API key")
    CLAUDE_API_KEY: str = Field(default="", description="Claude API key")
    DEFAULT_MODEL: str = Field(default="gpt-5", description="Default model")
    MODEL_TIMEOUT: int = Field(default=30, description="Model request timeout in seconds")
    
    # Database Configuration
    DATABASE_URL: str = Field(default="sqlite:///./data/ai_system.db", description="Database URL")
    DATABASE_POOL_SIZE: int = Field(default=10, description="Database pool size")
    DATABASE_ECHO: bool = Field(default=False, description="Echo SQL queries")
    
    # Cache Configuration
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis URL")
    CACHE_TTL: int = Field(default=3600, description="Cache TTL in seconds")
    
    # Authentication
    AUTH_SECRET_KEY: str = Field(default="secret-key-change-me", description="Secret key for JWT")
    AUTH_ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    AUTH_EXPIRATION_HOURS: int = Field(default=24, description="Token expiration hours")
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = Field(default=True, description="Enable rate limiting")
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = Field(default=60, description="Requests per minute limit")
    
    # Monitoring
    MONITORING_ENABLED: bool = Field(default=True, description="Enable monitoring")
    MONITORING_PROMETHEUS_PORT: int = Field(default=9090, description="Prometheus port")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Get settings instance (cached)
    """
    return Settings()
