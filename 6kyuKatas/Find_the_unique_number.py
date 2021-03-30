
def find_uniq(arr):
    for char in set(arr):
        if arr.count(char) == 1:
            return char
