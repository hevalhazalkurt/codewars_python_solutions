# CodeWars Python Solutions

---

## Find the capitals

Write a function that takes a single string (`word`) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

**Example:**

```Python
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
```


### Given Code


```python
def capitals(word):
    pass
```

---

### Solution 1


```python
def capitals(word):
    inds = []
    i = 0
    for l in word:
        if l.isupper():
            inds.append(i)
        i += 1
    return inds
```

---

### Solution 2


```python
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/539ee3b6757843632d00026b/)
