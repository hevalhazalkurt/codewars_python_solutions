# CodeWars Python Solutions

---

## Regexp Basics - is it a vowel?


Implement the function which should return `true` if given object is a vowel (meaning `a, e, i, o, u`), and `false` otherwise.

---

### Given Code


```python
def is_vowel(s):
    pass
```

---

### Solution


```python
def is_vowel(s):
    return s.lower() in ["a", "e", "i", "o", "u"] if len(s) > 0 else False
```

---


[See on CodeWars.com](https://www.codewars.com/kata/567bed99ee3451292c000025)
