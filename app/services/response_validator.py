import json
from fastapi import HTTPException
from typing import List
from pydantic import ValidationError
from app.schemas.text_schema import ErrorCorrection


def validate_response(response_content: str) -> List[ErrorCorrection]:

    try:
        # Parse the response content
        response_data = json.loads(response_content)
        

        # Validate JSON structure against ErrorCorrection schema
        error_corrections = []
        for sentence in response_data.get("sentences", []):
            error_correction = ErrorCorrection(**sentence)
            error_corrections.append(error_correction)

        return error_corrections

    except (ValueError, json.JSONDecodeError, ValidationError) as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid response format: {str(e)}"
        )
