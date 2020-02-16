# CodeWars Python Solutions

---

## Sum Arrays

Write a method `sum` (`sum_array` in python, `sumarray` in julia, `SumArray` in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.

**Examples**

```python
print sum_array([1 2 3])
> 6
print sum_array([])
> 0
```

**Assumptions**

- You can assume that you are only given numbers.
- You cannot assume the size of the array.
- You can assume that you do get an array and if the array is empty, return 0.


---

### Given Code


```python
def sum_array(a):
    pass
```

---

### Solution


```python
def sum_array(a):
    return sum(a)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/53dc54212259ed3d4f00071c/)
