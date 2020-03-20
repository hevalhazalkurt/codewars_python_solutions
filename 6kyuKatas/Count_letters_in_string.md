# CodeWars Python Solutions

---

## Count letters in string


In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.

**Example**

```python
letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
```




---

### Given Code


```python
def letter_count(s):
    pass
```

---

### Solution 1


```python
def letter_count(s):
    return {c: s.count(c) for c in s}
```

---

### Solution 2


```python
def letter_count(s):
    letters = {}
    for i in list(s):
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d)
