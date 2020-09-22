# CodeWars Python Solutions

---

## Numbers in strings


In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number.

For example, `solve("gh12cdy695m1") = 695`, because this is the largest of all number groupings.

Good luck!


---

### Given Code


```python
def solve(s):
    pass
```

---

### Solution


```python
def solve(s):
    for c in s:
        if c.isalpha():
            s = s.replace(c, " ")
    return max([int(i) for i in s.split(" ") if i != ""])
```

---




[See on CodeWars.com](https://www.codewars.com/kata/59dd2c38f703c4ae5e000014)
