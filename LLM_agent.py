from planner import planner
from retrievers import *
from refiner_cleaner import *


#the LLM Agent

cache={}

def agent(query, max_iters=3):
    if query in cache:
        return cache[query]
        
    query = planner(query)

    papers1 = search_papers(query)
    papers2 = search_openalex(query)

    papers = clean_papers(papers1 + papers2)

    if not papers:
        print("No papers found, trying broader search...")
        papers = search_papers(query + " research")

    papers = rank_papers(papers, query)
    papers = top_k(papers, 5)

    memory["papers"].extend(papers)
    cache[query]=papers
    return papers
