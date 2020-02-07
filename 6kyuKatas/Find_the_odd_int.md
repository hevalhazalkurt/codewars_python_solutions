# CodeWars Python Solutions

---

## Find the odd int

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

---

### Given Code


```python
def find_it(seq):
    pass
```

---

### Solution 1


```python
def find_it(seq):
    return min([n for n in seq if seq.count(n) % 2 != 0])
```

---



[See on CodeWars.com](https://www.codewars.com/kata/54da5a58ea159efa38000836)
