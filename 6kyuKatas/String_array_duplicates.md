# CodeWars Python Solutions

---

## String array duplicates


**Task**

In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

- `dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"]`
- `dup(["kelless","keenness"]) = ["keles","kenes"]`

Strings will be lowercase only, no spaces. See test cases for more examples.

Good luck!

---

### Given Code


```python
def dup(arry):
    pass
```

---

### Solution


```python
def dup(arry):
    news = []
    for w in arry:
        temp = []
        for i,t in enumerate(w):
            if t not in temp or t != temp[-1]:
                temp.append(t)
        news.append("".join(temp))
    return news
```

---


[See on CodeWars.com](https://www.codewars.com/kata/59f08f89a5e129c543000069)
