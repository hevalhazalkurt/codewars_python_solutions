
# Solution 1
def uncensor(infected, discovered):
    x = 0
    infected = list(infected)
    for e,c in enumerate(infected):
        if c == "*":
            infected[e] = discovered[x]
            x += 1
    return "".join(infected)





# Solution 2
def uncensor(infected, discovered):
    return infected.replace('*', '{}').format(*discovered)
