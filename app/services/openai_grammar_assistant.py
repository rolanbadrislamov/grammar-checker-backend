from fastapi import HTTPException
from typing import List
from openai import AsyncOpenAI
from app.schemas.text_schema import ErrorCorrection
from app.services.response_validator import validate_response
from app.core.config import settings
import asyncio


async def grammar_correction_assistant(text: str, retry_count: int = 3) -> List[ErrorCorrection]:
    for attempt in range(retry_count):
        try:
            client = AsyncOpenAI(
                api_key=settings.OPEN_AI_API_KEY)
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
                        "[errors, correct sentence, grammatical error types]. Nothing more. "
                        "Return [['No errors'], '{correct sentence}', ['No errors']], if you don't notice any errors in the sentence. "
                        "Format your response as a JSON in the example and don't shorten the sentences. "
                        "VERY IMPORTANT: DON'T FORGET NAMED FIELDS AND RETURN ALL SENTENCES. CONTRACTION IS NOT AN ERROR"
                        "Example: \n"
                        '{\n'
                        '  "sentences": [\n'
                        '    {\n'
                        '      "original": "She don\'t likes to eat pizza",\n'
                        '      "corrected": "She doesn\'t like to eat pizza",\n'
                        '      "errors": ["Don\'t likes to eat"],\n'
                        '      "error_types": ["Subject-verb agreement"]\n'
                        '    },\n'
                        '    {\n'
                        '      "original": "The dog chase it\'s tail every day.",\n'
                        '      "corrected": "The dog chases its tail every day.",\n'
                        '      "errors": "["Chase it\'s tail"]",\n'
                        '      "error_types": ["Subject-verb agreement", "Possessive pronoun"]\n'
                        '    },\n'
                        '    {\n'
                        '      "original": "The cat laying on the couch.",\n'
                        '      "corrected": "The cat is laying on the couch.",\n'
                        '      "errors": "["Laying on the couch"]",\n'
                        '      "error_types": ["Verb tense"]\n'
                        '    },\n'
                        '    {\n'
                        '      "original": "Because we expect the costs of large model API calls to decrease over time, we did not consider performance/cost trade-offs, reasoning that future models will likely have different tradeoffs and that today’s “most capable” models will be next year’s intermediate models in any case.",\n'
                        '      "corrected": "Because we expect the costs of large model API calls to decrease over time, we did not consider performance/cost trade-offs, reasoning that future models will likely have different tradeoffs and that today’s “most capable” models will be next year’s intermediate models in any case.",\n'
                        '      "errors": "["No errors"]",\n'
                        '      "error_types": ["No errors"]\n'
                        '    },\n'
                        '    {\n'
                        '      "orginal": "Hello, I am Rolan.",\n'
                        '      "corrected": "Hello, I am Rolan.",\n'
                        '      "errors": "["No errors"]",\n'
                        '      "error_types": ["No errors"]\n'
                        '    },\n'
                        '    {\n'
                        '      "original": "However, he doesn\'t like it",\n'
                        '      "corrected": "However, he doesn\'t like it",\n'
                        '      "errors": "["No errors"]",\n'
                        '      "error_types": ["No errors"]\n'
                        '    }\n'
                        '  ]\n'
                        '}\n'


                    )
                }
            ]

            response = await client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=2000,
                temperature=0.5,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )

            response_content = response.choices[0].message.content.strip()
            return validate_response(response_content)

        except Exception as e:
            if attempt < retry_count - 1:
                await asyncio.sleep(1)  # wait for a second before retrying
                continue
            else:
                raise HTTPException(
                    status_code=500, detail=f"Error occurred: {str(e)}")
