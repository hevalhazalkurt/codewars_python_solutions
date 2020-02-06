# CodeWars Python Solutions

---

## "Very Even" Numbers.

**Task**

Write a function that returns true if the number is a "Very Even" number.

If the number is odd, it is not a "Very Even" number.

If the number is even, return whether the sum of the digits is a "Very Even" number.

**Examples**

```python
input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd
input(222) => returns true
input(5) => returns false
```

---

### Given Code


```python
def is_very_even_number(n):
    return True
```

---

### Solution 1


```python
def is_very_even_number(n):
    return sum(map(int, str(n))) % 2 == 0 if n <= 10 else is_very_even_number(sum(map(int, str(n))))
```

---

### Solution 2


```python
def is_very_even_number(n):
    return (n - 1) % 9 % 2 != 0
```



---


[See on CodeWars.com](https://www.codewars.com/kata/58c9322bedb4235468000019)
