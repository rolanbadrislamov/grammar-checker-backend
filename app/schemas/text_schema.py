from pydantic import BaseModel
from typing import List


class TextInput(BaseModel):
    text: str


class ErrorCorrection(BaseModel):
    corrected: str
    errors: List[str]
    error_types: List[str]
