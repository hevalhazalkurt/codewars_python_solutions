# CodeWars Python Solutions

---

## Largest 5 digit number in a series

In the following 6 digit number:

```
283910
```

`91` is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:

```
1234567890
```

`67890` is the greatest sequence of 5 consecutive digits.

Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.


---

### Given Code


```python
def solution(digits):
    pass
```

---

### Solution


```python
def solution(digits):
    m = max(digits)
    possibles = []
    for e, d in enumerate(digits[:-4]):
        if d == m:
            possibles.append(int(digits[e:e+5]))
    return max(possibles)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/51675d17e0c1bed195000001)
