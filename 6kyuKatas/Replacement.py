# Solution 1
def sort_number(a):
    a = sorted(a)

    if a[-1] == 1:
        return a[:-1] + [2]
    else:
        return [1] + a[:-1]



### Solution 2
def sort_number(a):
    a = sorted(a)
    return [1]+a if a.pop()!=1 else a+[2]
