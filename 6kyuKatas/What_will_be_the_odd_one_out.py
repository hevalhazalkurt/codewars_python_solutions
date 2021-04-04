
# Solution 1
def odd_one_out(s):
    chars = {}
    for char in s:
        if char in chars:
            del chars[char]
        else:
            chars[char] = None
    return list(chars.keys())




# Solution 2
from collections import Counter

def odd_one_out(s):
    d = Counter(reversed(s))
    return [x for x in d if d[x] % 2][::-1]
