# CodeWars Python Solutions

---

## Count the divisors of a number

Count the number of divisors of a positive integer `n`.

Random tests go up to `n = 500000`.


**Examples**

```python
divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
```

---

### Given Code


```python
def divisors(n):
    pass
```

---

### Solution


```python
def divisors(n):
    return len([i for i in range(1, n+1) if n % i == 0])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/542c0f198e077084c0000c2e/)
