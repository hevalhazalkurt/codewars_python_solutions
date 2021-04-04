
# Solution 1
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)




# Solution 2
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
