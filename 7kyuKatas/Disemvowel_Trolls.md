# CodeWars Python Solutions

---

## Disemvowel Trolls


**Definition**

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string `"This website is for losers LOL!"` would become `"Ths wbst s fr lsrs LL!"`.

Note: for this kata `y` isn't considered a vowel.


---

### Given Code


```python
def disemvowel(string):
    return string
```

---

### Solution 1


```python
def disemvowel(string):
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])
```


---

### Solution 2


```python
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52fba66badcd10859f00097e)
