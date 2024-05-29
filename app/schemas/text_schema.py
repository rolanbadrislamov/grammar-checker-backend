from pydantic import BaseModel
from typing import List


# Define a Pydantic model for text input
class TextInput(BaseModel):
    text: str


# Define a Pydantic model for grammar checking output
class ErrorCorrection(BaseModel):
    # The corrected version of the text
    corrected: str

    # A list of errors found in the original text
    errors: List[str]

    # A list of error types corresponding to the errors
    error_types: List[str]
