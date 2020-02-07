# CodeWars Python Solutions

---

## Incorrect division method

This method, which is supposed to return the result of dividing its first argument by its second, isn't always returning correct values. Fix it.

---

### Given Code


```python
def divide_numbers(x,y):
    return x / y
```

---

### Solution 1


```python
def divide_numbers(x,y):
    return x / float(y)
```

---



[See on CodeWars.com](https://www.codewars.com/kata/54d1c59aba326343c80000e7)
