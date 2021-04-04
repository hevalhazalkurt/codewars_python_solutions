
def title_case(title, minor_words=''):
    words = []
    for w in title.split():
        if w.lower() not in minor_words.lower().split() or len(words) == 0:
            words.append(w.title())
        else:
            words.append(w.lower())
    return " ".join(words)
