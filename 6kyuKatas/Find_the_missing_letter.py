
def find_missing_letter(chars):
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ind = alp.find(chars[0])
    comp = alp[ind:ind+len(chars)+1]

    for e,i in enumerate(comp):
        if chars[e] != comp[e]:
            return comp[e]
