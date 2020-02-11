# CodeWars Python Solutions

---

## Sum of positive


**Definition**

You get an array of numbers, return the sum of all of the positives ones.

Example `[1,-4,7,12] => 1 + 7 + 12 = 20`

Note: if there is nothing to sum, the sum is default to `0`.

---

### Given Code


```python
def positive_sum(arr):
    pass
```

---

### Solution


```python
def positive_sum(arr):
    return sum([n for n in arr if n > 0])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5715eaedb436cf5606000381)
