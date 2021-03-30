
def greatest_product(n):
    mx = 0
    for i in range(len(n)+1):
        pr = 1
        for x in n[i:i+5]:
            if len(n[i:i+5]) < 5 or "0" in n[i:i+5]:
                break
            pr = pr * int(x)
        if pr > mx and pr != 1: mx = pr
    return mx
