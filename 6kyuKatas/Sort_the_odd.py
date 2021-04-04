
def sort_array(source_array):
    odds = sorted([n for n in source_array if n % 2 != 0])
    for n in source_array:
        if n % 2 == 0:
            odds.insert(source_array.index(n), n)
    return odds
