# Solution 1
def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()
    return "".join([w.capitalize() if w != words[0] else w for w in words])




# Solution 2
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
