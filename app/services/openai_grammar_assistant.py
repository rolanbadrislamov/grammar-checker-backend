import json
from fastapi import HTTPException
from typing import List
import openai
from app.schemas.text_schema import ErrorCorrection
from pydantic import BaseModel
from app.services.response_validator import validate_response


def grammar_correction_assistant(text: str) -> List[ErrorCorrection]:
    try:
        openai.api_key = ""
        model = "gpt-3.5-turbo"
        messages = [
            {
                "role": "system",
                "content": "You are an assistant that corrects grammar."
            },
            {
                "role": "user",
                "content": (
                    f"Correct the grammar in the following text: '{text}'. "
                    "For each incorrect sentence, return a list containing three values: "
                    "[wrong sentence, correct sentence, grammatical error types]. Nothing more. "
                    "Return ['{wrong sentence}', '{correct sentence}', ['No errors']], if you don't notice any errors in the sentence. "
                    "Format your response as a JSON in the example and don't shorten the sentences."
                    "Example: \n"
                    '{\n'
                    '  "sentences": [\n'
                    '    {\n'
                    '      "original": "She don\'t likes to eat pizza.",\n'
                    '      "corrected": "She doesn\'t like to eat pizza.",\n'
                    '      "errors": ["subject-verb agreement", "contraction"]\n'
                    '    },\n'
                    '    {\n'
                    '      "original": "The dog chase it\'s tail everyday.",\n'
                    '      "corrected": "The dog chases its tail every day.",\n'
                    '      "errors": ["subject-verb agreement", "possessive pronoun"]\n'
                    '    },\n'
                    '    {\n'
                    '      "original": "The cat laying on the couch.",\n'
                    '      "corrected": "The cat is laying on the couch.",\n'
                    '      "errors": ["verb tense"]\n'
                    '    },\n'
                    '    {\n'
                    '      "original": "Hello, my name is Rolan.",\n'
                    '      "corrected": "Hello, my name is Rolan.",\n'
                    '      "errors": ["No errors"]\n'
                    '    }\n'
                    '  ]\n'
                    '}\n'
                )
            }
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=500,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        response_content = response.choices[0].message['content'].strip()
        return validate_response(response_content)


    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occurred: {str(response_content)}")
