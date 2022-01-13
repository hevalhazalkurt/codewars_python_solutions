# CodeWars Python Solutions

---

## Mutual Recursion

Mutual Recursion allows us to take the fun of regular recursion (where a function calls itself until a terminating condition) and apply it to multiple functions calling each other!

Let's use the Hofstadter Female and Male sequences to demonstrate this technique. You'll want to create two functions `F` and `M` such that the following equations are true:

```
F(0) = 1
M(0) = 0
F(n) = n - M(F(n - 1))
M(n) = n - F(M(n - 1))
```

Don't worry about negative numbers, `n` will always be greater than or equal to zero.

Hofstadter Wikipedia Reference http://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Female_and_Male_sequences

---

### Given Code


```python
def f(n):
    pass

def m(n):
    pass
```

---

### Solution


```python
def f(n):
    if n == 0:
        return 1
    else:
        return n - m(f(n-1))

def m(n):
    if n == 0:
        return 0
    else:
        return n - f(m(n-1))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b/)
