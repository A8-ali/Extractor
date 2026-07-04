import json
import os

from api_client import call_api
from schema import SCHEMA
from errors import ExtractionError

def build_prompt(text: str) -> str:
    """
    Build the prompt for the AI model.
    """
    schema = json.dumps(
        {key: str(value) for key, value in SCHEMA.items()},
        indent=4,)
    return f"""
You are an AI that extracts structured information from resumes.

Return ONLY valid JSON.

Schema:

{schema}

Rules:

-Return ONLY JSON.
-Do not use markdown.
-Do not use triple backticks.
-Do not use extra word befor or after the json
- If age is unknown, return null.
- Otherwise, age must be an integer.

- name is a string
- email is a string
- phone is a string
- linkedin is a string
- github is a string
- skills is an array of strings
- education is an array of strings
- experience is an array of strings

If information is missing:

- use "" for strings
- use [] for arrays

Resume:

{text}
"""


def parse_response(response: str) -> dict:
    """
    Convert AI response into a Python dictionary.
    """

    try:
        return json.loads(response)

    except json.JSONDecodeError as e:
        raise ExtractionError("Invalid JSON returned by AI.") from e


def extract_info(text: str) -> dict:
    """
    Extract structured information from resume text.

    Args:
        text: extracted text from PDF

    Returns:
        Parsed resume information as a dictionary
    """

    prompt = build_prompt(text)

    response = call_api(prompt)

    data = parse_response(response)

    return data