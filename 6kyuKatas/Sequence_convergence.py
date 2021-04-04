
def next(num):
    mul = 1
    for c in str(num):
        if c!="0":
            mul *= int(c)
    return num + mul

def convergence(n):
    base = 1
    test = n
    count = 0
    while test!=base:
        if test > base:
            base = next(base)
        else:
            test =next(test)
            count +=1
    return count
