from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing the router from the application API module
from app.api.api_v1.router import router
# Importing the settings configuration
from app.core.config import settings

# Creating a FastAPI application instance with specified title and OpenAPI URL
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"  # OpenAPI schema path
)

# Adding CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,  # List of allowed origins for CORS
    # Allow credentials (cookies, authorization headers, etc.)
    allow_credentials=True,
    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],
    allow_headers=["*"],  # Allow all headers
)

# Including the router with a prefix for API versioning
app.include_router(router, prefix=settings.API_V1_STR)
