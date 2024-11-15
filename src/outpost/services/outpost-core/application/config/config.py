from __future__ import annotations
import os
from dotenv import load_dotenv





class Settings:
    # load the environment variables
    load_dotenv()

    # get the environment variables
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT  = (os.getenv("REDIS_PORT"))

    # the database url
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///outpost.db")




settings = Settings()
