
def dup(arry):
    news = []
    for w in arry:
        temp = []
        for i,t in enumerate(w):
            if t not in temp or t != temp[-1]:
                temp.append(t)
        news.append("".join(temp))
    return news
