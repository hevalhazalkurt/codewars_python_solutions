# CodeWars Python Solutions

---

## Sum without highest and lowest number

Take 2 strings `s1` and `s2` including only letters from `a` to `z`. Return a new sorted string, the longest possible, containing distinct letters,

- each taken only once - coming from s1 or s2.


**Examples**

```python
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

---

### Given Code


```python
def sum_array(arr):
    pass
```

---

### Solution


```python
def sum_array(arr):
    return 0 if arr == None  or len(arr) < 3 else sum(arr) - (max(arr) + min(arr))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5656b6906de340bd1b0000ac/)
