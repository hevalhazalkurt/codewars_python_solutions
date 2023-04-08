# CodeWars Python Solutions

---

## Between Extremes

Given an array of numbers, return the difference between the largest and smallest values.

For example:

`[23, 3, 19, 21, 16]` should return 20 (i.e., 23 - 3).

`[1, 434, 555, 34, 112]` should return 554 (i.e., 555 - 1).

The array will contain a minimum of two elements. Input data range guarantees that max-min will cause no integer overflow.

---

### Given Code


```python
def between_extremes(numbers):
    #Your code goes here!
    pass
```

---

### Solution 1


```python
def between_extremes(numbers):
    return max(numbers) - min(numbers)
```


---

### Solution 2


```python
def between_extremes(numbers):
    max = None
    min = None
    for n in numbers:
        if max is None:
            max = n
            min = n
        elif n > max:
            max = n
        elif n < min:
            min = n
    return max - min
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56d19b2ac05aed1a20000430/)
