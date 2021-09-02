# CodeWars Python Solutions

---

## Pyramid Array

Write a function that when given a number >= 0, returns an Array of ascending length subarrays.


```
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
```

Note: the subarrays should be filled with `1`s

---

### Given Code


```python
def pyramid(n):
    pass
```

---

### Solution


```python
def pyramid(n):
    return [[1 for _ in range(i)] for i in range(1,n+1)]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/515f51d438015969f7000013/)
