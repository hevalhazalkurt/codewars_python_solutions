# CodeWars Python Solutions

---

## Find the stray number

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

**Examples**

```
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
```

---

### Given Code


```python
def stray(arr):
    pass
```

---

### Solution 


```python
def stray(arr):
    return [num for num in arr if arr.count(num) == 1][0]
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/57f609022f4d534f05000024)
