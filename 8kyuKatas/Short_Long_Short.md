# CodeWars Python Solutions

---

## Short Long Short

Given 2 strings, `a` and `b`, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

Hint for R users:

The length of string is not always the same as the number of characters
For example: (Input1, Input2) --> output

```
("1", "22") --> "1221"
("22", "1") --> "1221"
```

---

### Given Code


```python
def solution(a, b):
    pass

```

---

### Solution


```python
def solution(a, b):
    sorted_by_len = list(sorted([a, b], key=len))
    return f"{sorted_by_len[0]}{sorted_by_len[1]}{sorted_by_len[0]}"
```

---


[See on CodeWars.com](https://www.codewars.com/kata/50654ddff44f800200000007/)