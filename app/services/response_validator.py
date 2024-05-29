import json
from fastapi import HTTPException
from typing import List
from pydantic import ValidationError
from app.schemas.text_schema import ErrorCorrection


# Function to validate and parse the response content
def validate_response(response_content: str) -> List[ErrorCorrection]:
    try:
        # Parse the response content from JSON string to a Python dictionary
        response_data = json.loads(response_content)

        # List to hold validated ErrorCorrection objects
        error_corrections = []

        # Iterate over each sentence in the response data
        for sentence in response_data.get("sentences", []):
            # Validate the sentence structure against the ErrorCorrection schema
            error_correction = ErrorCorrection(**sentence)
            # Add the validated ErrorCorrection object to the list
            error_corrections.append(error_correction)

        # Return the list of validated ErrorCorrection objects
        return error_corrections

    except (ValueError, json.JSONDecodeError, ValidationError) as e:
        # Raise an HTTPException with status code 400 if there's an error in parsing or validation
        raise HTTPException(
            status_code=400, detail=f"Invalid response format: {str(e)}"
        )
