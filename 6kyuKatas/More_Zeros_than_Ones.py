
def more_zeros(s):
    chars = [c for c in s if bin(ord(c)).count("0") >= 5]
    uniques = []

    for char in chars:
        if char not in uniques: uniques.append(char)

    return uniques
