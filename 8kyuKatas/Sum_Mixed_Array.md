# CodeWars Python Solutions

---

## Sum Mixed Array


Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.



---

### Given Code


```python
def sum_mix(arr):
    #your code here
```

---

### Solution 1


```python
def sum_mix(arr):
    return sum([int(n) for n in arr])
```

---

### Solution 2


```python
def sum_mix(arr):
    return sum(map(int, arr))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57eaeb9578748ff92a000009)
