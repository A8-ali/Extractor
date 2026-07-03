import json
import os
import requests

from schema import SCHEMA
from errors import APIError, ExtractionError
from config import (
    API_KEY,
    API_ENDPOINT,
    MODEL,
)
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


def call_api(prompt: str) -> str:
    """
    Send the prompt to OpenRouter.
    """

    if not API_KEY:
        raise APIError("API key not found.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        API_ENDPOINT,
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        raise APIError(response.text)

    return response.json()["choices"][0]["message"]["content"]


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