from gemini_guider import *


def chat_response(query):
    res = client.models.generate_content(
        model=MODEL_NAME,
        contents=query
    )
    return res.text