# CodeWars Python Solutions

---

## char_to_ascii


Take a string and return a hash with all the ascii values of the characters in the string. Returns nil if the string is empty. The key is the character, and the value is the ascii value of the character. Repeated characters are to be ignored and non-alphebetic characters as well.

---

### Given Code


```python
def char_to_ascii(string):
    pass
```

---

### Solution


```python
def char_to_ascii(string):
    return {c:ord(c) for c in string if c != " " and c.isalpha()} if len(string) else None
```



---


[See on CodeWars.com](https://www.codewars.com/kata/55e9529cbdc3b29d8c000016)
