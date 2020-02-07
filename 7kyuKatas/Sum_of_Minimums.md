# CodeWars Python Solutions

---

## Sum of Minimums!

Given an 2D list of size `m * n`. Your task is to find the sum of minimum value in each row.


**Examples**

```python
[
  [1,2,3,4,5], # minimum value of row is 1
  [5,6,7,8,9], # minimum value of row is 5
  [20,21,34,56,100] # minimum value of row is 20
]
```

So, the function should return `26` because sum of minimums is as `1 + 5 + 20 = 26`

Note: You will be always given non-empty list containing Positive values.

---

### Given Code


```python
def sum_of_minimums(numbers):
    pass
```

---

### Solution 1


```python
def sum_of_minimums(numbers):
    return sum([min(nums) for nums in numbers])
```

---

### Solution 2


```python
def sum_of_minimums(numbers):
    return sum(map(min, numbers))
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5d5ee4c35162d9001af7d699)
