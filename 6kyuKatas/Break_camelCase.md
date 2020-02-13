# CodeWars Python Solutions

---

## Break camelCase


**Definition**

Complete the solution so that the function will break up camel casing, using a space between words.


```Python
solution("camelCasing")  ==  "camel Casing"
```

---

### Given Code


```python
def solution(s):
    pass
```

---

### Solution


```python
def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5208f99aee097e6552000148)
