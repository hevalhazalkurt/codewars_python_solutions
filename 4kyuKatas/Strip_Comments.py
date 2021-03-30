# Solution 1
def solution(string,markers):
    s_list = string.split("\n")
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.strip())
    return "\n".join(n_list)



# Solution 2
def solution(string,markers):
    s_list = string.split('\n')
    for marker in markers:
        s_list = [item.split(marker)[0].strip() for item in s_list]
    return '\n'.join(s_list)
