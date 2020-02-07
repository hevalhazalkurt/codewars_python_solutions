# CodeWars Python Solutions

---

## What's the real floor?

**Task Overview**

Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor ('cause of superstition).

Write a function that given an American floor (passed as an integer) returns the real floor.
Moreover, your function should work for basement floors too: just return the same value as the passed one.


**Usage Examples** :

```python
get_real_floor(1) == 0
get_real_floor(0) == 0 # Special case to please Europeans
get_real_floor(5) == 4
get_real_floor(15) == 13
get_real_floor(-3) == -3
```

---

### Given Code


```python
def get_real_floor(n):
    # code here
```

---

### Solution 1


```python
def get_real_floor(n):
    if n <= 0:
        return n
    elif n >= 13:
        return n-2
    else:
        return n - 1
```


---

### Solution 2


```python
def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2
```


---


[See on CodeWars.com](https://www.codewars.com/kata/574b3b1599d8f897470018f6)
