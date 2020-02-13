# CodeWars Python Solutions

---

## Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


---

### Given Code


```python
def move_zeros(array):
    pass
```

---

### Solution


```python
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/52597aa56021e91c93000cb0/)
