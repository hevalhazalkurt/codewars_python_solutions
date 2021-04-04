
def expanded_form(num):
    s = []
    i = len(str(num)) -1
    for n in str(num):
        if n != "0":
            s.append(n + "0" * i)
        i -= 1
    return " + ".join(s)
