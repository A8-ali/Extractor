import os

def get_api_key() -> str:
    API_KEY = os.getenv("AI_API_KEY")
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY environment variable not found.")

    return API_KEY

API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.1-8b-instruct"
API_KEY = get_api_key()