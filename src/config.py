"""Configuration settings for the backend service."""

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.db.url import normalize_database_url


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    API_TITLE: str = "AI Powered Assessment Backend"
    API_VERSION: str = "0.1.0"

    DATABASE_URL: str
    JWT_SECRET: str = Field(min_length=32)
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4"

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    LOG_LEVEL: str = "INFO"

    @field_validator("CORS_ORIGINS")
    @classmethod
    def validate_cors_origins(cls, origins: list[str]) -> list[str]:
        if "*" in origins:
            raise ValueError("CORS_ORIGINS must contain explicit origins, not '*'")
        return origins

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def use_psycopg_driver(cls, database_url: str) -> str:
        return normalize_database_url(database_url)


settings = Settings()
