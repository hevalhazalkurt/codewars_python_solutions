
def namelist(names):
    if len(names) == 0 : return ""
    elif len(names) == 1 : return names[0]['name']
    else : return ", ".join([names[i]['name'] for i in range(len(names)-1)]) + " & " + names[-1]['name']
