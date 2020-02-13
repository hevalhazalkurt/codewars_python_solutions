# CodeWars Python Solutions

---

## Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)

- `HH` = hours, padded to 2 digits, range: 00 - 99
- `MM` = minutes, padded to 2 digits, range: 00 - 59
- `SS` = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (`99:59:59`)

You can find some examples in the test fixtures.

---

### Given Code


```python
def make_readable(seconds):
    pass
```

---

### Solution 1


```python
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"
```

---


### Solution 2


```python
def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/52685f7382004e774f0001f7/)
