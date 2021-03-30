# Solution 1
def camel_case(string):
    return "".join([w.title() for w in string.split()])



# Solution 2
def camel_case(string):
    return string.title().replace(" ", "")
