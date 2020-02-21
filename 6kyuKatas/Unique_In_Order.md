# CodeWars Python Solutions

---

## Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

**For example**

```python
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```

---

### Given Code


```python
def unique_in_order(iterable):
    pass
```

---

### Solution 


```python
def unique_in_order(iterable):
    chars = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i-1]:
            chars.append(iterable[i])
    return chars
```


---


[See on CodeWars.com](https://www.codewars.com/kata/54e6533c92449cc251001667/)
