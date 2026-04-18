#Checking the intention of the user, basically intent detection

def detect_intent(query):
    q = query.lower()

    triggers = [
        "write a paper",
        "write research",
        "create research paper",
        "generate paper",
        "draft paper",
        "help me create one",
        "Can you help me create a research paper"
    ]

    if any(t in q for t in triggers):
        return "research"
    
    return "summary"