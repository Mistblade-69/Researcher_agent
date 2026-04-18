from planner import MODEL_NAME,client
from trimmer import trim_text

def summarize(papers):
    text = "\n\n".join([
        f"{i+1}. {p['title']}\n{trim_text(p.get('summary') or '')}"
        for i, p in enumerate(papers)
    ])

    prompt = f"""
Summarize each paper giving their title and small summaries of 5-6 lines
{text}
"""
    res = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return res.text

#citations
def citations(papers):
    return [f"{p['title']} ({p.get('link','')})" for p in papers]