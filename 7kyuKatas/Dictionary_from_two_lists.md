# CodeWars Python Solutions

---

## Dictionary from two lists

There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. Write a function `createDict(keys, values)` that returns a dictionary created from keys and values. If there are not enough values, the rest of keys should have a `None` (JS `null`) value. If there not enough keys, just ignore the rest of values.


**Example 1**

```python
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
```


**Example 2**

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
```

---

### Given Code


```python
def createDict(keys, values):
    pass
```

---

### Solution 1


```python
def createDict(keys, values):
    d = {}
    for e,i in enumerate(keys):
        if e < len(values):
            d[i] = values[e]
        else:
            d[i] = None
    return d
```


### Solution 2


```python
def createDict(keys, values):
    return {k:(values[e] if e<len(values) else None) for e,i in enumerate(keys)}
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5533c2a50c4fea6832000101)
