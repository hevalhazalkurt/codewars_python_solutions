
# Solution 1
def find_it(seq):
    return min([n for n in seq if seq.count(n) % 2 != 0])




# Solution 2
def find_it(seq):
    return [i for i in seq if seq.count(i) % 2 != 0][0]
