def make_snippet(sentence):
    words = sentence.split()
    if len(words) > 5:
        snippet = " ".join(words[0:5])
        snippet += "..."
    else:
        snippet = sentence
        
    return snippet

def count_words(sentence):
    return len(sentence.split())
