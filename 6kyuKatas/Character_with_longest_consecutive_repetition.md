# CodeWars Python Solutions

---

## Character with longest consecutive repetition


**Task**

For a given string `s` find the character `c` (or `C`) with longest consecutive repetition and return:


```
(c, l)
```


where `l` (or `L`) is the length of the repetition. If there are two or more characters with the same `l` return the first in order of appearance.

For empty string return:

```
('', 0)
```

---

### Given Code


```python
def longest_repetition(chars):
    pass
```

---

### Solution


```python
def longest_repetition(chars):
    if len(chars) == 0:
        return ("",0)
    else:
        temp = ""
        for i in range(len(chars)):
            if i == 0:
                temp = chars[i]
            elif temp[-1] == chars[i]:
                temp = temp + chars[i]
            else:
                temp = temp + " " + chars[i]
        temp = sorted(temp.split(" "), reverse=True, key=len)    
        return (*set(temp[0]),len(temp[0]))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/586d6cefbcc21eed7a001155)
