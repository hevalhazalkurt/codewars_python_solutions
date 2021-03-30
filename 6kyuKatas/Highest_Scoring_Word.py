
# Solution 1
def high(x):
    alp = "abcdefghijklmnopqrstuvwxyz"
    counter = [sum([alp.find(i) + 1 for i in w]) for w in x.split()]
    return x.split()[counter.index(max(counter))]




# Solution 2
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
