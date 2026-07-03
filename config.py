import os

def get_api_key() -> str:
    api_key = os.getenv("AI_API_KEY")
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY environment variable not found.")

    return api_key

API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.1-8b-instruct"
API_KEY = get_api_key()