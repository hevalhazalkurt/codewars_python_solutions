# CodeWars Python Solutions

---

## Two Oldest Ages

The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items.

**Examples**

```python
two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]
```

---

### Given Code


```python
def two_oldest_ages(ages):
    pass
```

---

### Solution


```python
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/511f11d355fe575d2c000001/)
