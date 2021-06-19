# CodeWars Python Solutions

---

## Quarter of the year


**Definition**

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

---

### Given Code


```python
def quarter_of(month):
    # your code here
```

---

### Solution 1


```python
def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
```

---

### Solution 2


```python
def quarter_of(month):
    return (month + 2) // 3
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5ce9c1000bab0b001134f5af)
