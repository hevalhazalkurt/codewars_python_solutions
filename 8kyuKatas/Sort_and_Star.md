# CodeWars Python Solutions

---

## Sort and Star

You will be given an vector of string(s). You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have `"***"` between each of its letters.

You should not remove or add elements from/to the array.

---

### Given Code


```python
def two_sort(array):
    pass
```

---

### Solution 1


```python
def two_sort(array):
    return "***".join([c for c in sorted(array)[0]])
```

---

### Solution 2


```python
def two_sort(array):
    return "***".join(min(array))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/)
