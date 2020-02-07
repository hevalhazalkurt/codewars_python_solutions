# CodeWars Python Solutions

---

## Beginner Series # 2 Clock

Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.


**Examples**

```python
past(0, 1, 1) == 61000
```

Note! h, m and s will be only Natural numbers!


---

### Given Code


```python
def past(h, m, s):
    pass
```

---

### Solution 1


```python
def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)
```


---

### Solution 2


```python
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a)
