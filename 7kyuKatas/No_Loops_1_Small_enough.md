# CodeWars Python Solutions

---

## No Loops 2 - You only need one


**No Loops Allowed**

You will be given an array `(a)` and a limit value `(limit)`. You must check that all values in the array are below or equal to the limit value. If they are, return `True`. Else, return `False`.

You can assume all values in the array are numbers.

Do not use loops. Do not modify input array.

Looking for more, loop-restrained fun? Check out the other kata in the series:

https://www.codewars.com/kata/no-loops-2-you-only-need-one

https://www.codewars.com/kata/no-loops-3-copy-within




---

### Given Code


```python
def small_enough(a, limit):
    # your code here
    pass
```

---

### Solution


```python
def small_enough(a, limit): 
    return max(a) <= limit
```

---


[See on CodeWars.com](https://www.codewars.com/kata/no-loops-1-small-enough)
