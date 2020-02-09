# CodeWars Python Solutions

---

## Exes and Ohs


**Definition**

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.


**Examples:**

```Python
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```

---

### Given Code


```python
def xo(s):
    pass
```

---

### Solution 1


```python
def xo(s):
    return (s.lower()).count("x") == (s.lower()).count("o")
```


---

### Solution 2


```python
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55908aad6620c066bc00002a)
