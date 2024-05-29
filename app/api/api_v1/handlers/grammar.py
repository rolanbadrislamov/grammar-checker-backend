from fastapi import APIRouter, HTTPException
from app.schemas.text_schema import TextInput, ErrorCorrection
from app.services.openai_grammar_assistant import grammar_correction_assistant
from typing import List

# Create a router instance for grammar-related endpoints
grammar_router = APIRouter()


# Define an API endpoint for checking grammar
@grammar_router.post("/check-grammar", response_model=List[ErrorCorrection])
async def grammar_check(input_text: TextInput):

    # Check if input text is empty
    if not input_text.text.strip():
        raise HTTPException(status_code=400, detail="Input text is empty")

    try:
        # Call the grammar correction function asynchronously
        error_corrections = await grammar_correction_assistant(input_text.text)

        # Return the error corrections
        return error_corrections
    except Exception as e:
        # Raise an HTTPException if an internal server error occurs
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}"
        )
