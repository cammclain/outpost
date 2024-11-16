from __future__ import annotations
import os
from dotenv import load_dotenv

from pydantic import BaseSettings

from pydantic import Field, AnyHttpUrl, ValidationError
from pydantic.config import BaseSettings

class Settings(BaseSettings):
    # Environment variables with types and optional default values
    REDIS_HOST: str
    REDIS_PORT: int
    DATABASE_URL: AnyHttpUrl = Field(default="sqlite:///outpost.db")
    SESSION_SECRET_KEY: str

    class Config:
        # Specify the `.env` file location
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
