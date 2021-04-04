
def simplify(number):
    number = str(number)
    if len(number) == 1:
        if number == "0":
            return ""
        else:
            return number

    l = len(number) -1
    n = []

    for c in number[:-1]:
        if c != "0":
            n.append("{}*1{}".format(c, "0"*l))
        l -= 1

    return "+".join(n) + "+" + number[-1] if number[-1] != "0" else "+".join(n)
