
def calc(x):
    total1 = "".join([str(ord(i)) for i in x])
    total2 = total1.replace("7", "1")
    return sum([int(i) for i in total1]) - sum([int(i) for i in total2])
