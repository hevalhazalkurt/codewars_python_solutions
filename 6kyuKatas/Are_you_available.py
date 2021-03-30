
def check_availability(schedule, current_time):
    for t in schedule:
        start, finish = t[0], t[1]
        if int(start[:2]) <= int(current_time[:2]) <= int(finish[:2]) and int(current_time[3:]) < int(finish[3:]):
            return t[1]
    else:
        return True
