# CodeWars Python Solutions

---

## Return the closest number multiple of 10

Given a number return the closest number to it that is divisible by 10.

**Example Input**

```
22
25
37
```

**Expected Output**


```
20
30
40
```

---

### Given Code


```python
def closest_multiple_10(i):
    pass
```

---

### Solution 1


```python
def closest_multiple_10(i):
    return i - i % 10 if i % 10 < 5 else i - i % 10 + 10
```

---

### Solution 2


```python
def closest_multiple_10(i):
    return round(i, -1)
```



---


[See on CodeWars.com](https://www.codewars.com/kata/58249d08b81f70a2fc0001a4)
