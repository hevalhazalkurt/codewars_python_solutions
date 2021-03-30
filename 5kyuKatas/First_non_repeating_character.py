
def first_non_repeating_letter(string):
    reps = [c for c in string if string.lower().count(c.lower()) == 1]
    return  reps[0] if len(reps) > 0 else ""
