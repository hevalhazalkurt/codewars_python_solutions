# CodeWars Python Solutions

---

## Highest Scoring Word

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.


---

### Given Code


```python
def high(x):
    pass
```

---

### Solution 1


```python
def high(x):
    alp = "abcdefghijklmnopqrstuvwxyz"
    counter = [sum([alp.find(i) + 1 for i in w]) for w in x.split()]
    return x.split()[counter.index(max(counter))]
```

### Solution 2


```python
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
```



---


[See on CodeWars.com](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/)
