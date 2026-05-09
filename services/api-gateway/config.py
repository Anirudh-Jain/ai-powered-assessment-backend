"""Configuration for API Gateway service."""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # API
    API_TITLE: str = "AI Assessment Platform - API Gateway"
    API_VERSION: str = "0.1.0"
    
    # Services
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL", "http://auth:8001")
    EXAM_SERVICE_URL: str = os.getenv("EXAM_SERVICE_URL", "http://exam:8002")
    QUESTION_SERVICE_URL: str = os.getenv("QUESTION_SERVICE_URL", "http://question:8003")
    GRADING_SERVICE_URL: str = os.getenv("GRADING_SERVICE_URL", "http://grading:8004")
    SUBMISSION_SERVICE_URL: str = os.getenv("SUBMISSION_SERVICE_URL", "http://submission:8005")
    
    # CORS
    CORS_ORIGINS: list = ["*"]
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"


settings = Settings()
