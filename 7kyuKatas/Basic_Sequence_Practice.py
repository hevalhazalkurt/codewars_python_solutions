
def sum_of_n(n):
    if n < 0:
        return sorted([sum(x for x in range(i,1)) for i in range(n, 1)], reverse=True)
    else:
        return [sum([x for x in range(i+1)]) for i in range(n+1)]
