
### Solution 1
def digital_root(n):
    return n if n < 10 else digital_root(sum([int(num) for num in str(n)]))




### Solution 2
def digital_root(n):
    sums = sum([int(num) for num in str(n)])
    if len(str(sums)) >= 2:
        sums = digital_root(sums)
    return sums
