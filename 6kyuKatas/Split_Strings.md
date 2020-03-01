# CodeWars Python Solutions

---

## Split Strings

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore (`'_'`).

Examples:


```python
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
```



---

### Given Code


```python
def solution(s):
    pass
```

---

### Solution 1


```python
def solution(s):
    ls = [s[i:i+2] for i,c in enumerate(s) if i % 2 == 0 and len(s[i:i+2]) == 2]
    if len(s) % 2 != 0:
        ls.append(s[-1] + "_")
    return ls
```

---

### Solution 2


```python
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/)
