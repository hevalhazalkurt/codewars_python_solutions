# CodeWars Python Solutions

---

## Reversed sequence

Get the number `n` (n>0) to return the reversed sequence from `n` to `1`.

Example :

```
n=5 >> [5,4,3,2,1]
```

---

### Given Code


```python
def reverse_seq(n):
    pass
```

---

### Solution


```python
def reverse_seq(n):
    return sorted([i for i in range(1, n+1)], reverse=True)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5a00e05cc374cb34d100000d)
