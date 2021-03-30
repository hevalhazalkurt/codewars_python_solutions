
def nexus(users):
    return min(sorted(users), key=lambda x: abs(x - users[x]))
