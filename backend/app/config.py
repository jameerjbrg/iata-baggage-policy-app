import os
from pathlib import Path
from pydantic_settings import BaseSettings

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # API Configuration
    API_TITLE: str = "IATA Baggage Policy Search API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Enterprise baggage policy search powered by official IATA standards"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/iata_baggage.db"
    SQLALCHEMY_ECHO: bool = False
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # File paths
    DATA_DIR: str = str(BASE_DIR / "data")
    LOGS_DIR: str = str(BASE_DIR / "logs")
    PDF_FILE_PATH: str = str(BASE_DIR / "data" / "iata_baggage_standards.pdf")
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = str(BASE_DIR / "logs" / "app.log")
    AUDIT_LOG_FILE: str = str(BASE_DIR / "logs" / "audit_log.json")
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Ensure required directories exist
os.makedirs(settings.DATA_DIR, exist_ok=True)
os.makedirs(settings.LOGS_DIR, exist_ok=True)
