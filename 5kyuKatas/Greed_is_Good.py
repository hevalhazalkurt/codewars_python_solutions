
def score(dice):
    from collections import Counter
    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)

    tot = 0

    for k,v in dices.items():
        if v >= 3:
            tot += points[k] * (v // 3)
        if k == 1:
            tot += 100 * (v % 3)
        elif k == 5:
            tot += 50 * (v % 3)

    return tot
