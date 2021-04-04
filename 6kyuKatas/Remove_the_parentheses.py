
import re
def remove_parentheses(s):
    while re.findall(r"\([^()]*\)", s):
        s = re.sub(r"\([^()]*\)", "", s)
    return s
