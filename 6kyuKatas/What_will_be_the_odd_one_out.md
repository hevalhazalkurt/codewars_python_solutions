# CodeWars Python Solutions

---

## What will be the odd one out?

Write a function that will take in a string and return all the unpaired characters (show up an odd number of times in the string) in the order they were encountered as an array. In case of multiple options to choose from, take the last occurence as the unpaired character.


**Notes**

- A wide range of characters is used, and some of them may not render properly in your browser.
- Your solution should be linear in terms of string length to pass the last test.


**Examples**

```python
odd_one_out('Hello World')   ==  ["H", "e", " ", "W", "r", "l", "d"]
odd_one_out('Codewars')      ==  ["C", "o", "d", "e", "w", "a", "r", "s"]
odd_one_out('woowee')        ==  []
odd_one_out('wwoooowweeee')  ==  []
odd_one_out('racecar')       ==  ["e"]
odd_one_out('Mamma')         ==  ["M"]
odd_one_out('Mama')          ==  ["M", "m"]
```

---

### Given Code


```python
def odd_one_out(s):
    pass
```

---

### Solution 1


```python
def odd_one_out(s):
    chars = {}
    for char in s:
        if char in chars:
            del chars[char]
        else:
            chars[char] = None
    return list(chars.keys())
```

---

### Solution 2


```python
from collections import Counter

def odd_one_out(s):
    d = Counter(reversed(s))
    return [x for x in d if d[x] % 2][::-1]
```



---


[See on CodeWars.com](https://www.codewars.com/kata/55b080eabb080cd6f8000035)
