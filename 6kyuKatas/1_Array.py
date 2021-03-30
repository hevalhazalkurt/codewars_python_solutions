
def up_array(arr):
    if len(arr) < 1 :
        return None

    for i in arr:
        if len(str(i)) > 1 or i < 0:
            return None
    else:
        return [int(i) for i in str(int("".join([str(n) for n in arr]))+1)]
