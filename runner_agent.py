#Agent running code
from LLM_agent import agent
from research_generator import *
from summarizer import *
from explainer import *


def run_agent(query):
    intent = input("Enter mode (summary 1/ research 2): ").lower() #use input module here
    papers = agent(query)
    

    if intent == "research" or "2":
        print(generate_research(query, papers))
    else:
        print("Summary:\n")
        print(summarize(papers))
        

        print("\nCitations:\n")
        for i, c in enumerate(citations(papers), 1):
            print(f"{i}.", c)
            if papers[i-1].get("pdf"):
                print("   PDF:", papers[i-1]["pdf"])

        choice = input("\nEnter paper number to explain (or press Enter to skip): ")

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(papers):
                print("\nExplanation:\n")
                print(explain_paper(papers[idx]))


topic=input("\n\n Hi User, Enter the topic you would search for: ")

print(run_agent(f"{topic}"))