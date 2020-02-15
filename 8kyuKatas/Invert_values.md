# CodeWars Python Solutions

---

## Invert values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.


```python
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

You can assume that all values are integers. Do not mutate the input array/list.

---

### Given Code


```python
def invert(lst):
    pass
```

---

### Solution


```python
def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/)
