from gemini_guider import *

#paper explainer

def explain_paper(papers):
    text = papers.get("summary") or papers.get("title")

    prompt = f"Explain this paper briefly and concise:\n{text}"
    
    res = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return res.text