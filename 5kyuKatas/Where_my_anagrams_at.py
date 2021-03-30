# Solution 1

def anagrams(word, words):
    return [i for i in words if set(i) == set(word) and len(i) == len(word)]



# Solution 2
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]
