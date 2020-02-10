# CodeWars Python Solutions

---

## Grasshopper - Summation


**Definition**

Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

**Example**

```
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
```

---

### Given Code


```python
def summation(num):
    pass
```

---

### Solution


```python
def summation(num):
    return sum([n for n in range(num+1)])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55d24f55d7dd296eb9000030)
