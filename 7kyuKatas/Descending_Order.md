# CodeWars Python Solutions

---

## Descending Order

Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


**Examples**

Input: `21445` Output: `54421`

Input: `145263` Output: `654321`

Input: `123456789` Output: `987654321`


---

### Given Code


```python
def descending_order(num):
    pass
```

---

### Solution


```python
def descending_order(num):
    return int("".join(sorted([num for num in str(num)], reverse=True)))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5467e4d82edf8bbf40000155/)
