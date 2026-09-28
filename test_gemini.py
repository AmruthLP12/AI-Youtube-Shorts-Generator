from google import genai
from google.genai import types

from shorts_generator.config import (
    GEMINI_MODEL,
    require_gemini_key,
)


client = genai.Client(api_key=require_gemini_key())

print(f"Testing model: {GEMINI_MODEL}")

response = client.models.generate_content(
    model=GEMINI_MODEL,
    contents='Return exactly this JSON: {"status": "ok"}',
    config=types.GenerateContentConfig(
        temperature=0,
        response_mime_type="application/json",
        max_output_tokens=100,
    ),
)

print("SUCCESS")
print(response.text)
