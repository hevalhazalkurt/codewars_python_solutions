# CodeWars Python Solutions

---

## Tracking Sums in a Process

Observe the process with the array given below and the tracking of the sums of each corresponding array.

```
[5, 3, 6, 10, 5, 2, 2, 1] (34) ----> [5, 3, 6, 10, 2, 1] ----> (27) ------> [10, 6, 5, 3, 2, 1]  ----> [4, 1, 2, 1, 1] (9) -----> [4, 1, 2] (7)
```

The tracked sums are : `[34, 27, 9, 7]`. We do not register one of the sums. It is not difficult to see why.

We need the function `track_sum` ( or `trackSum` ) that receives an array ( or list ) and outputs a tuple ( or array ) with the following results in the order given below:

* array with the tracked sums obtained in the process
* final array

So for our example given above, the result will be:


```
track_sum([5, 3, 6, 10, 5, 2, 2, 1]) == [[34, 27, 9, 7], [4, 1, 2]]
```

You will find more cases in the Example Tests.


---

### Given Code


```python
def track_sum(arr):
    # your code here
    return [[], []]
```

---

### Solution 1


```python
def track_sum(arr):
    sums = []
    sums.append(sum(arr))
    sums.append(sum(set(arr)))

    rev = sorted([i for i in set(arr)], reverse=True)
    dec = [rev[e]-rev[e+1] for e,i in enumerate(rev[1:])]
    sums.append(sum(dec))

    n = dec[0]
    last = [n]

    for i in dec:
        if i not in last:
            last.append(i)
            n = i

    sums.append(sum(last))

    return [sums, last]
```

---

### Solution 2


```python
def track_sum(arr):
    a = arr
    b = sorted(set(a), reverse=True)
    c = [(x-y) for (x,y) in zip(b,b[1:])]
    d = sorted(set(c), key=c.index)
    return [list(map(sum,[a,b,c,d])), d]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56dbb6603e5dd6543c00098d/)
