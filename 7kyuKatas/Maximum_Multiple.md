# CodeWars Python Solutions

---

## Maximum Multiple

**Task**

Given a `Divisor` and a `Bound` , Find the largest integer `N` , Such That ,


**Conditions**

* `N` is divisible by divisor
* `N` is less than or equal to bound
* `N` is greater than 0.


**Notes**

* The parameters (`divisor`, `bound`) passed to the function are only positive values .
* It's guaranteed that a divisor is Found .


**Examples**

```
maxMultiple (2,7) ==> return (6)
maxMultiple (10,50)  ==> return (50)
maxMultiple (37,200) ==> return (185)
```

**Explanation**

- (6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .
- (50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .
- (185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .

---

### Given Code


```python
def max_multiple(divisor, bound):
    #your code here
```

---

### Solution 1


```python
def max_multiple(divisor, bound):
    return max([num for num in range(bound+1) if num % divisor == 0])
```

---

### Solution 2


```python
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
```


-------

[See on CodeWars.com](https://www.codewars.com/kata/57f609022f4d534f05000024)
