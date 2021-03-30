
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
