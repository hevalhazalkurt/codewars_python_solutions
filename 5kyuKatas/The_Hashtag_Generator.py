
def generate_hashtag(s):
    return "#" + "".join([w.strip().title() for w in s.split()]) if 140 > len(s) > 1 else False
