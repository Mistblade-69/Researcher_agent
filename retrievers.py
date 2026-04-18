#retriever using semantic scholar
import requests

memory ={
    "papers":[],
    "queries":[]
}

#doing the openalex better
def parse_abstract(inv_idx):
    if not inv_idx:
        return ""
    
    words = sorted(
        [(pos, word) for word, positions in inv_idx.items() for pos in positions]
    )
    
    return " ".join([w for _, w in words])

def search_papers(query):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    params = {
        "year"  : "2020-2026", 
        "query" : query,
        "limit" : 20,
        "fields": "title,abstract,openAccessPdf, url",
        "source": "semantic scholar"
    }
    
    res = requests.get(url, params=params)

    if res.status_code !=200:
        print("Semantic error:", res.status_code)
        data = res.json()

    papers = []
    for p in data.get("data", []):
        papers.append({
            "title": p.get("title"),
            "summary": p.get("abstract"),
            "pdf": (p.get("openAccessPdf") or {}).get("url"),
            "link": p.get("url")
        })
    
    return papers


def search_openalex(query):
    url = "https://api.openalex.org/works"
    
    params = {
        "search": query,
        "per-page": 5
    }
    
    res = requests.get(url, params=params)

    if res.status_code != 200:
        print("OpenAlex error:", res.status_code)
        return []

    try:
        data = res.json()
    except:
        print("Invalid JSON response")
        return []

    papers = []
    for p in data.get("results", []):
        papers.append({
            "title": p.get("title"),
            "summary": parse_abstract(p.get("abstract_inverted_index")),
            "pdf": p.get("primary_location", {}).get("pdf_url"),
            "link": p.get("id")
        })
    
    return papers