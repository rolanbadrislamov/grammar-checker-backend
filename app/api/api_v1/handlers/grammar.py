from fastapi import APIRouter, HTTPException
from app.schemas.text_schema import TextInput, ErrorCorrection
from app.services.openai_grammar_assistant import grammar_correction_assistant
from typing import List

grammar_router = APIRouter()

# API endpoint to check grammar


@grammar_router.post("/check-grammar", response_model=List[ErrorCorrection])
async def grammar_check(input_text: TextInput):
    try:
        # Call grammar check function
        error_corrections = await grammar_correction_assistant(input_text.text)
        return error_corrections
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}")
