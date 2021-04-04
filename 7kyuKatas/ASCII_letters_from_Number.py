
def convert(number):
    return "".join([chr(int(number[e:e+2])) for e in range(0,len(number),2)])
