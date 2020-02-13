# CodeWars Python Solutions

---

## Beginner - Reduce but Grow

Given a non-empty array of integers, return the result of multiplying the values together in order.

Example:

```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

---

### Given Code


```python
def grow(arr):
    pass
```

---

### Solution


```python
def grow(arr):
    m = 1
    for n in arr:
        m *= n
    return m
```


---


[See on CodeWars.com](https://www.codewars.com/kata/57f780909f7e8e3183000078)
