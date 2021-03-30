
def narcissistic( value ):
    return value == sum([int(n) ** len(str(value)) for n in str(value)])
