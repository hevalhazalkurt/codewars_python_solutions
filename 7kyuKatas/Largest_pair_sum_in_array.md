# CodeWars Python Solutions

---

## Largest pair sum in array

**Task**

Given a sequence of numbers, find the largest pair sum in the sequence.

For example

```
[10, 14, 2, 23, 19] --> 42 (i.e. sum of 23 and 19)
[99, 2, 2, 23, 19]  --> 122 (i.e. sum of 99 and 23)
```

Input sequence contains minimum two elements and every element is an integer.


---

### Given Code


```python
def largest_pair_sum(numbers):
    pass
```

---

### Solution


```python
def largest_pair_sum(numbers):
    return sum(sorted(numbers)[-2:])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/556196a6091a7e7f58000018)
