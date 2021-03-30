
# Solution 1
def meeting(s):
    return "".join(sorted(["({}, {})".format(i[1].upper(),i[0].upper()) for i in [n.split(":") for n in s.split(";")]]))




# Solution 2
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
