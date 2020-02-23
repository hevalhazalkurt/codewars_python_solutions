# CodeWars Python Solutions

---

## Largest Elements

Write a program that outputs the top `n` elements from a list.


```python
largest(2, [7,6,5,4,3,2,1])
# => [6,7]
```



### Given Code


```python
def largest(n,xs):
    pass
```

---

### Solution


```python
def largest(n,xs):
  return sorted(sorted(xs, reverse=True)[:n])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53d32bea2f2a21f666000256/)
