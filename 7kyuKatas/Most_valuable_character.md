# CodeWars Python Solutions

---

## Most valuable character


**Description:**

In this Kata, you will be given a string and your task is to return the most valuable character. The value of a character is the difference between the index of its last occurrence and the index of its first occurrence. Return the character that has the highest value. If there is a tie, return the lexicographically lowest character.

All inputs will be lower case.

For example:

```
solve('a') = 'a'
solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
solve("axyzxyz") = 'x'
```


---

### Given Code


```python
def solve(st):
    pass
```

---

### Solution


```python
def solve(st):
    chars = {char: abs(st.find(char) - st.rfind(char)) for char in st}
    return max(sorted(chars), key=lambda x: chars[x])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5dd5128f16eced000e4c42ba)
