
def in_array(array1, array2):
    arr = []
    for a2 in array2:
        for a1 in array1:
            if a1 in a2 and a1 not in arr:
                arr.append(a1)
    return sorted(arr)
