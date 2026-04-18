


#Paper cleaning mechanism
def clean_papers(papers):
    seen = set()
    unique = []

    for p in papers:
        if p["title"] not in seen:
            seen.add(p["title"])
            unique.append(p)
    
    return unique[:10]

#more Scoring
def score_paper(p, query):
    title = (p.get("title") or "").lower()
    summary = (p.get("summary") or "").lower()
    
    score = 0
    for word in query.lower().split():
        if word in title:
            score += 2
        if word in summary:
            score += 1
    
    return score

#ranking paper mechansim

def rank_papers(papers, query):
    return sorted(
        papers, 
        key=lambda p: (
            score_paper(p,query),
            p.get("year", 0)
        ),
        reverse=True)

#ranking papers in k

def top_k(papers, k=5):
    return papers[:k]

#Query refiner

def refine_query(query):
    return query + " research paper"