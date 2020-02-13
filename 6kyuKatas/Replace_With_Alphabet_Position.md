# CodeWars Python Solutions

---

## Replace With Alphabet Position

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.


**Example**


```python
alphabet_position("The sunset sets at twelve o' clock.")
```

Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` (as a string)

---

### Given Code


```python
def alphabet_position(text):
    pass
```

---

### Solution


```python
def alphabet_position(text):
    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/546f922b54af40e1e90001da)
