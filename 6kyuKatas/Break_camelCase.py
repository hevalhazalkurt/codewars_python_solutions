
def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])
