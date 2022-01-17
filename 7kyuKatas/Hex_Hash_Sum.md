# CodeWars Python Solutions

---

## Hex Hash Sum

Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of the numbers in the hex strings (ignore letters).


**Examples**


```
"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
```


---

### Given Code


```python
def hex_hash(code):
    pass
```

---

### Solution


```python
def hex_hash(code):
    return sum([sum([int(i) for i in hex(ord(c)) if i.isdigit()]) for c in code for i in c])
```

---



[See on CodeWars.com](https://www.codewars.com/kata/5ab363ff6a176b29880000dd)
