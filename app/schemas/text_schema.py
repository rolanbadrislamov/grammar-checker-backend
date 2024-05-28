from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str


class ErrorCorrection(BaseModel):
    original: str
    corrected: str
    errors: List[str]