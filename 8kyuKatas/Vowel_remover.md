# CodeWars Python Solutions

---

## Vowel remover


Create a function called `shortcut` to remove all the lowercase vowels in a given string.

**Example**

```python
shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
```

Don't worry about uppercase vowels.


---

### Given Code


```python
def shortcut( s ):
    pass
```

---

### Solution 1


```python
def shortcut( s ):
    return "".join([char for char in s if char not in "aeiou"])
```

---

### Solution 2


```python
def shortcut(s):
    return s.translate(None, 'aeiou')
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5547929140907378f9000039)
