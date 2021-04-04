
### Solution 1
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))



### Solution 2
def sequence_sum(begin_number, end_number, step):
    n = (end_number - begin_number) // step
    return 0 if n < 0 else (n+1)*(n*step+begin_number+begin_number)//2
