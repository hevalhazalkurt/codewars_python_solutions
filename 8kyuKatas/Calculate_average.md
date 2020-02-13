# CodeWars Python Solutions

---

## Calculate average

Write function avg which calculates average of numbers in given list.

Python:

* Due to rounding issues please do not use `statistics.mean` or such.
* If the array is empty, return 0.

**Examples**


```python
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
```


---

### Given Code


```python
# create an array called websites that has "codewars" as its only value
```

---

### Solution


```python
def find_average(array):
    return sum(array) // len(array)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57a2013acf1fa5bfc4000921)
