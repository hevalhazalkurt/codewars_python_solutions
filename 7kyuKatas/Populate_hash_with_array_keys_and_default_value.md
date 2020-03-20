# CodeWars Python Solutions

---

## Populate hash with array keys and default value


Complete the function so that it takes an array of keys and a default value and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value.


**Examples**


```python
["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}
```



---

### Given Code


```python
def populate_dict(keys, default):
    pass
```

---

### Solution 1


```python
def populate_dict(keys, default):
    return {i:default for i in keys}
```

---

### Solution 2


```python
def populate_dict(keys, default):
    return dict.fromkeys(keys, default)
```



---


[See on CodeWars.com](https://www.codewars.com/kata/51c38e14ea1c97ffaf000003)
