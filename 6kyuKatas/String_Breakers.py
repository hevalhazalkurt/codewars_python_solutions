
### Solution 1
def string_breakers(n, st):
    new = []
    for e,i in enumerate(list(st.replace(" ", ""))):
        if e != 0 and e % n == 0:
            new.append("\n")
            new.append(i)
        else:
            new.append(i)
    return "".join(new)




### Solution 2
def string_breakers(n, st):
    s = st.replace(" ", "")
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n))
