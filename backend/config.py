"""Configuration settings for the backend service."""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_TITLE: str = "AI Powered Assessment Backend"
    API_VERSION: str = "0.1.0"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://assessmentuser:assessmentpass123@postgres:5432/assessment_db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = "gpt-4"

    CORS_ORIGINS: list[str] = ["*"]
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    class Config:
        env_file = ".env"


settings = Settings()
