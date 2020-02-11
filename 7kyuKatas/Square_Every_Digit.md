# CodeWars Python Solutions

---

## Square Every Digit


**Definition**

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

Note: The function accepts an integer and returns an integer

---

### Given Code


```python
def square_digits(num):
    pass
```

---

### Solution


```python
def square_digits(num):
    return int("".join([str(int(n)**2) for n in str(num)]))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/546e2562b03326a88e000020)
