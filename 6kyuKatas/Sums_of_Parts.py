
### Solution 1
def parts_sums(ls):
    cop = list(ls)
    top = sum(ls)
    sums = 0
    parts = []
    for i in range(len(ls)):
        if len(parts) == 0:
            parts.append(top)
        else:
            parts.append(top - sums)
        sums += cop[i]
    parts.append(0)
    return parts




### Solution 2
def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1]-i)
    return sums
