
def pig_it(text):
    return " ".join(["{}{}ay".format(c[1:], c[0]) if c.isalpha() else c for c in text.split()])
