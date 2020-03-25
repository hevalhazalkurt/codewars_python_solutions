# CodeWars Python Solutions

---

## Combine objects


Your task is to write a function that takes two or more objects and returns a new object which combines all the input objects.

All input object properties will have only numeric values. Objects are combined together so that the values of matching keys are added together.

**An example**


```python
objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
combine(objA, objB) # Returns { a: 13, b: 20, c: 36, d: 3 }
```

The combine function should be a good citizen, so should not mutate the input objects.

---

### Given Code


```python
def combine():
    pass
```

---

### Solution


```python
def combine(*args):
    comb = {}
    for d in args:
        for k,v in d.items():
            if k in comb:
                comb[k] += v
            else:
                comb[k] = v
    return comb
```



---


[See on CodeWars.com](https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819)
