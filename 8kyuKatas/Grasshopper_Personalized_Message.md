# CodeWars Python Solutions

---

## Grasshopper - Personalized Message


Create a function that gives a personalized greeting. This function takes two parameters: `name` and `owner`.

Use conditionals to return the proper message:


| case |	return |
|--|--|
| name equals owner	| `'Hello boss'` |
| otherwise	| `'Hello guest'` |


---

### Given Code


```python
def greet(name, owner):
    pass
```

---

### Solution


```python
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5772da22b89313a4d50012f7/)
