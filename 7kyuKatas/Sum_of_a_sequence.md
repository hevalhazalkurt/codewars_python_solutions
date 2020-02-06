# CodeWars Python Solutions

---

## Sum of a sequence


Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: `begin`, `end`, `step`.

If `begin` value is greater than the end, function should returns `0`



**Examples**

```
sequenceSum(2,2,2) === 2
sequenceSum(2,6,2) === 12 // 2 + 4 + 6
sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequenceSum(1,5,3) === 5 // 1 + 4
```

This is the first kata in the series:

1) Sum of a sequence (this kata)
2) [Sum of a Sequence [Hard-Core Version]](https://www.codewars.com/kata/sum-of-a-sequence-hard-core-version/javascript)


---

### Given Code


```python
def sequence_sum(begin_number, end_number, step):
    #your code here
```

---

### Solution


```python
def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number+1, step)])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/586f6741c66d18c22800010a)
