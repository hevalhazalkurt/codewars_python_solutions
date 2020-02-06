# CodeWars Python Solutions

---

## Remove duplicate words

Your task is to remove all duplicate words from a string, leaving only single (first) words entries.


**Example:**

***Input:***

`'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'`

***Output:***

`'alpha beta gamma delta'`


---

### Given Code


```python
def remove_duplicate_words(s):
    pass
```

---

### Solution 1


```python
def remove_duplicate_words(s):
    l = []
    for word in s.split():
        if word not in l:
            l.append(word)
    return " ".join(l)
```

---

### Solution 2


```python
def remove_duplicate_words(s):
    return " ".join(sorted(set(s.split()), key = s.index))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5b39e3772ae7545f650000fc)
