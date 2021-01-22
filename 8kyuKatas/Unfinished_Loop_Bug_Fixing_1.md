# CodeWars Python Solutions

---

## Unfinished Loop - Bug Fixing # 1

Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!


---

### Given Code


```python
def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res
```

---

### Solution


```python
def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55c28f7304e3eaebef0000da)
