import requests

from config import (
    API_KEY,
    API_ENDPOINT,
    MODEL,
)

from errors import APIError


def call_api(prompt: str) -> str:
    """
    Send prompt to OpenRouter and return response text.
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
                "content": prompt,
            }
        ],
    }

    response = requests.post(
        API_ENDPOINT,
        headers=headers,
        json=payload,
        timeout=60,
    )

    if response.status_code != 200:
        raise APIError(response.text)

    return response.json()["choices"][0]["message"]["content"]