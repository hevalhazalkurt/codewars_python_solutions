
def longest_repetition(chars):
    if len(chars) == 0:
        return ("",0)
    else:
        temp = ""
        for i in range(len(chars)):
            if i == 0:
                temp = chars[i]
            elif temp[-1] == chars[i]:
                temp = temp + chars[i]
            else:
                temp = temp + " " + chars[i]
        temp = sorted(temp.split(" "), reverse=True, key=len)
        return (*set(temp[0]),len(temp[0]))
