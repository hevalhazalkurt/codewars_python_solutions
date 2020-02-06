# CodeWars Python Solutions

---

## Sum of two lowest positive integers

**Task**


Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like `[19, 5, 42, 2, 77]`, the output should be `7`.

`[10, 343445353, 3453445, 3453545353453]` should return `3453455`.


**Explanation**



---

### Given Code


```python
def sum_two_smallest_numbers(numbers):
    #your code here
```

---

### Solution


```python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/558fc85d8fd1938afb000014)
