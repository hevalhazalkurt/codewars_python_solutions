
# Solution 1
def create_phone_number(n):
    s = "".join([str(i) for i in n])
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"




# Solution 2
def create_phone_number(n):
    return "({}{}{} {}{}{}-{}{}{}{})".format(*n)
