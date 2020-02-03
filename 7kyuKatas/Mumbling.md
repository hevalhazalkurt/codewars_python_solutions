# CodeWars Python Solutions

---

## Mumbling


This time no story, no theory. The examples below show you how to write function `accum`:

**Examples**

```python
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of `accum` is a string which includes only letters from `a..z` and `A..Z`.

---

### Given Code


```python
def accum(s):
    # your code here
```

---

### Solution


```python
def accum(s):
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])
```


-------

[See on CodeWars.com](https://www.codewars.com/kata/5667e8f4e3f572a8f2000039)
