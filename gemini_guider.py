import os 
from google import genai

GEMINI_API_KEY="api_key"
client=genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME="gemini-flash-lite-latest"
