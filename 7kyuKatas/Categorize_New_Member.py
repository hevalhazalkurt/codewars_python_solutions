
def openOrSenior(data):
    return ["Senior" if person[0] >= 55 and person[1] > 7 else "Open" for person in data]
