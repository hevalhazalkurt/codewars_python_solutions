# CodeWars Python Solutions

---

## Find all occurrences of an element in an array


Given an array (a list in Python) of integers and an integer `n`, find all occurrences of `n` in the given array and return another array containing all the index positions of `n` in the given array.

If `n` is not in the given array, return an empty array `[]`.

Assume that `n` and all values in the given array will always be integers.

**Example:**

```python
find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]
```


---

### Given Code


```python
def find_all(array, n):
    pass
```

---

### Solution


```python
def find_all(array, n):
    return [e for e,i in enumerate(array) if i == n]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/59a9919107157a45220000e1)
