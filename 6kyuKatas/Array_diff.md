# CodeWars Python Solutions

---

## Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list `a`, which are present in list `b`.


```
array_diff([1,2],[1]) == [2]
```


If `a` value is present in `b`, all of its occurrences must be removed from the other:


```
array_diff([1,2,2,2,3],[2]) == [1,3]
```

---

### Given Code


```python
def array_diff(a, b):
    pass
```

---

### Solution 1


```python
def array_diff(a, b):
    if len(b) == 0:
        return a

    for i in b:
        if i in a:
            for n in range(a.count(i)):
                a.remove(i)
    return a
```

---

### Solution 2


```python
def array_diff(a, b):
    return [i for i in a if i not in b]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/523f5d21c841566fde000009/)
