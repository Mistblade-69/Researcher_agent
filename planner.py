#Planner module
from gemini_guider import *

def planner(query):
    prompt = f"""
    Improve this research query as better as possible leading for more enhanced academic paper search adn only wihtin its domain.
    Make it more specific and include semantics for the given keyword along with relevant ones.
    Do not change the topic

    Query: {query}
    Return one improved query.
    """
    
    res=client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return res.text.strip()