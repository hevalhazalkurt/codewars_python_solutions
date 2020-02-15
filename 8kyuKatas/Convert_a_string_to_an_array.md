# CodeWars Python Solutions

---

## Convert a string to an array

Write a function to split a string and convert it into an array of words. For example:


```python
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```


---

### Given Code


```python
def string_to_array(s):
    pass
```

---

### Solution


```python
def string_to_array(s):
    return s.split() if len(s) > 0 else [""]
```

---



[See on CodeWars.com](https://www.codewars.com/kata/57e76bc428d6fbc2d500036d)
