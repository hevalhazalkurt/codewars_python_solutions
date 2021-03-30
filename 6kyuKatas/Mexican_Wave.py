
def wave(people):
    if len(people) == 0:
        return []
    else:
        people = people.lower()
        the_waves = []
        for e,i in enumerate(people):
            if i == " ":
                continue
            else:
                the_waves.append(people[:e] + people[e].upper() + people[e+1:])
        return the_waves
