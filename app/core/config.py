from typing import List

from pydantic import AnyHttpUrl, BaseSettings
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        os.getenv("FRONTEND_URL")
    ]
    PROJECT_NAME: str = "Grammar-Checker-Backend"
    # Retrieve the API key from environment variables
    OPEN_AI_API_KEY: str = os.getenv("API_KEY")


settings = Settings()
