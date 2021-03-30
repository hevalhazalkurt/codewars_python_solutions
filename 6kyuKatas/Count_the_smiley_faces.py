
def count_smileys(arr):
    smileys = []
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            smileys.append(s)
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            smileys.append(s)
    return len(smileys)
