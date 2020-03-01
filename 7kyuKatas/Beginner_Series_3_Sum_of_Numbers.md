# CodeWars Python Solutions

---

## Beginner Series # 3 Sum of Numbers

Given two integers `a` and `b`, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return `a` or `b`.

Note: `a` and `b` are not ordered!

Example:

```python
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
```


---

### Given Code


```python
def get_sum(a,b):
    pass
```

---

### Solution


```python
def get_sum(a,b):
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55f2b110f61eb01779000053/)
