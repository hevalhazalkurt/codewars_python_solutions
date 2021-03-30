# Solution 1
def dashatize(n):
    print(n)
    if type(n) == int:
        n = str(abs(n))
        new = ""
        for e,i in enumerate(n):
            if int(i) % 2 != 0:
                if e == 0:
                    new += "{}-".format(i)
                elif e == len(n)-1:
                    new += "-{}".format(i)
                else:
                    new += "-{}-".format(i)
            else:
                new += i
        if new[-1] == "-": new = new[:-1]
        return new.replace("--", "-")
    else:
        return "None"





# Solution 2
def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')
