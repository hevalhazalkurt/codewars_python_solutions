# CodeWars Python Solutions

---

## Search for letters

Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

The objective is to set each of the 26 characters of the output string to either `'1'` or `'0'` based on the fact whether the `N`th letter of the alphabet is present in the input (independent of its case).

So if an `'a'` or an `'A'` appears anywhere in the input string (any number of times), set the first character of the output string to `'1'`, otherwise to `'0'`. if `'b'` or `'B'` appears in the string, set the second character to `'1'`, and so on for the rest of the alphabet.

For instance:

```
"a   **&  cZ"  =>  "10100000000000000000000001"
```


---

### Given Code


```python
def change(st):
    pass
```

---

### Solution


```python
def change(st):
    alp = "abcdefghijklmnopqrstuvwxyz"
    return "".join(["1" if c in st or c.upper() in st else "0" for c in alp]) if len(st) else "00000000000000000000000000"

```

---


[See on CodeWars.com](https://www.codewars.com/kata/52dbae61ca039685460001ae)
