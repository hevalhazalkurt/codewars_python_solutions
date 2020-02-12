# CodeWars Python Solutions

---

## Find The Parity Outlier


**Definition**

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.


**Examples**

```Python
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

---

### Given Code


```python
def find_outlier(integers):
    pass
```

---

### Solution


```python
def find_outlier(integers):
    odds = [i for i in integers if i % 2 != 0]
    evens = [i for i in integers if i % 2 == 0]
    return odds[0] if len(odds) == 1 else evens[0]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)
