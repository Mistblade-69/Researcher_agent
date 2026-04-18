import os 
from google import genai

GEMINI_API_KEY="AIzaSyB4D4z_NZHYE3bajnDCwOYtAvN5MrvLhq0"
client=genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME="gemini-flash-lite-latest"