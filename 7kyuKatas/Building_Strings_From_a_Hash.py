
def solution(pairs):
    return ",".join(sorted(["{} = {}".format(k,v) for k,v in pairs.items()]))
