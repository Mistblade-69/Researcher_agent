#Research generator function
from gemini_guider import MODEL_NAME,client
from trimmer import trim_text

def generate_research(topic, papers):
    text = "\n\n\n".join([trim_text(p["summary"]) for p in papers])

    prompt = f"""
    Write a structured research draft on: {topic}

    Use:
    {text}

    Include:
    - Abstract
    - Introduction
    - Methodology
    - Conclusion
    """

    res = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return res.text