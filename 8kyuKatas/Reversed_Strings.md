# CodeWars Python Solutions

---

## Reversed Strings


Complete the solution so that it reverses the string value passed into it.

```python
solution('world') # returns 'dlrow'
```

---

### Given Code


```python
def solution(string):
    pass
```

---

### Solution 1


```python
def solution(string):
    return string[::-1]
```

---

### Solution 2


```python
def solution(string):
    return "".join([l for l in string][::-1])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5168bb5dfe9a00b126000018)
