# CodeWars Python Solutions

---

## Form The Minimum

**Task**

Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).


**Conditions**

Only positive integers will be passed to the function (> 0 ), no negatives or zeros.



**Examples**

```
minValue ({1, 3, 1})  ==> return (13)
minValue({5, 7, 5, 9, 7})  ==> return (579)
minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
```

**Explanation**

- (13) is the minimum number could be formed from {1, 3, 1} , Without duplications
- (579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications
- (134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications

---

### Given Code


```python
def min_value(digits):
    # your code here
```

---

### Solution 1


```python
def min_value(digits):
    return int("".join(sorted(list(set([str(num) for num in digits])))))
```

---

### Solution 2


```python
def min_value(digits):
    return "".join(map(str, sorted(set(digits))))
```


-------

[See on CodeWars.com](https://www.codewars.com/kata/5ac6932b2f317b96980000ca)
