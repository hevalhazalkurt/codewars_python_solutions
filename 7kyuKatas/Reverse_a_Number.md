# CodeWars Python Solutions

---

## Reverse a Number

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

**Examples**

```Python
123 ->  321
-456 -> -654
1000 ->    1
```


### Given Code


```python
def reverse_number(n):
    pass
```

---

### Solution


```python
def reverse_number(n):
    return int(str(n)[::-1]) if n > 0 else int(str(n * -1)[::-1]) * -1
```


---


[See on CodeWars.com](https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/)
