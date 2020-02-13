# CodeWars Python Solutions

---

## If you can't sleep, just count sheep!!

If you can't sleep, just count sheep!!


**Task**:

Given a non-negative integer, `3` for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`. Input will always be valid, i.e. no negative integers.


---

### Given Code


```python
def count_sheep(n):
    pass
```

---

### Solution 1


```python
def count_sheep(n):
    count = ""
    for i in range(1, n+1):
        count = count + "{} sheep...".format(i)
    return count
```


---

### Solution 2


```python
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5b077ebdaf15be5c7f000077)
