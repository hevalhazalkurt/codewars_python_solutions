# CodeWars Python Solutions

---

## Scramblies

Complete the function `scramble(str1, str2)` that returns `true` if a portion of `str1` characters can be rearranged to match `str2`, otherwise returns `false`.

**Notes:**

- Only lower case letters will be used (a-z). No punctuation or digits will be included.
- Performance needs to be considered


`Input strings s1 and s2 are null terminated.`


**Examples**


```python
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```


---

### Given Code


```python
for c in set(s2):
    pass
```

---

### Solution


```python
for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
```

---


[See on CodeWars.com](https://www.codewars.com/kata/55c04b4cc56a697bb0000048)
