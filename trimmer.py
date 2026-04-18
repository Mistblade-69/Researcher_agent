#text triming

def trim_text(text, max_words=100):
    return " ".join(text.split()[:max_words])