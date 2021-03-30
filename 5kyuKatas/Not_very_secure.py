# Solution 1
def alphanumeric(password):
    return " " not in password and len([c for c in password if c.isdigit() or c.isalpha()]) == len(password) and len(password) > 0



# Solution 2
def alphanumeric(string):
    return string.isalnum()
