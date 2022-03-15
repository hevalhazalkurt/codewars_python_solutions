def ips_between(start, end):
    s_list = [int(s) for s in start.split('.')]
    e_list = [int(e) for e in end.split('.')]
    power = [3, 2, 1, 0]
    result = 0
    for index in range(4):
        result += (e_list[index] - s_list[index]) * (256 ** power[index])
    return result
