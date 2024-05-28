from fastapi import APIRouter
from app.api.api_v1.handlers import grammar

router = APIRouter()

router.include_router(grammar.grammar_router, tags=["grammar"])
