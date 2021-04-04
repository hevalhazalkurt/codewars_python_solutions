
def char_to_ascii(string):
    return {c:ord(c) for c in string if c != " " and c.isalpha()} if len(string) else None
