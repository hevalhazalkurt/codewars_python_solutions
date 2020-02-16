# CodeWars Python Solutions

---

## Regex count lowercase letters


Your task is simply to count the total number of lowercase letters in a string.

**Examples**

```python
lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123"); ===> 3

lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3

lowercaseCount(""); ===> 0;

lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0

lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26
```

---

### Given Code


```python
def lowercase_count(strng):
    pass
```

---

### Solution 1


```python
def lowercase_count(strng):
    i = 0
    for c in strng:
        if c.islower():
            i += 1
    return i
```

---

### Solution 2


```python
def lowercase_count(strng):
    return sum(a.islower() for a in strng)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56a946cd7bd95ccab2000055/)
