# CodeWars Python Solutions

---

## No zeros for heros

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

```
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
```

Zero alone is fine, don't worry about it. Poor guy anyway


---

### Given Code


```python
def no_boring_zeros(n):
    pass
```

---

### Solution 1


```python
def no_boring_zeros(n):
    if n == 0:
        return 0
    else:
        n = str(n)
        while n[-1] == "0":
            n = n[:-1]
        return int(n)
```

---


### Solution 2


```python
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0
```

---


[See on CodeWars.com](https://www.codewars.com/kata/570a6a46455d08ff8d001002)
