from typing import List

from pydantic import AnyHttpUrl, BaseSettings
import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# Define a Settings class for configuration using Pydantic's BaseSettings
class Settings(BaseSettings):
    # API base path
    API_V1_STR: str = "/api/v1"

    # List of allowed CORS origins, retrieved from environment variables
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        os.getenv("FRONTEND_URL")
    ]

    # Name of the project
    PROJECT_NAME: str = "Grammar-Checker-Backend"

    # Retrieve the API key for OpenAI from environment variables
    OPEN_AI_API_KEY: str = os.getenv("API_KEY")


# Instantiate the Settings class to create a settings object
settings = Settings()
