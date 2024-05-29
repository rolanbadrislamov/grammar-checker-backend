from fastapi import APIRouter
from app.api.api_v1.handlers import grammar

# Create a new APIRouter instance
router = APIRouter()

# Include the grammar router, tagging it with "Grammar"
router.include_router(grammar.grammar_router, tags=["Grammar"])
