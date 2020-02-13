# CodeWars Python Solutions

---

## Testing 1-2-3

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is `n: string`. Notice the colon and space in between.


**Examples**


```python
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
```


---

### Given Code


```python
def number(lines):
    pass
```

---

### Solution


```python
def number(lines):
    return ["{}: {}".format(str(i+1), c) for i,c in enumerate(lines)]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9)
