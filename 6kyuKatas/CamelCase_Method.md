# CodeWars Python Solutions

---

## CamelCase Method

Write simple .camelCase method (`camel_case` function in PHP, `CamelCase` in C# or `camelCase` in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:


```python
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
```


---

### Given Code


```python
def camel_case(string):
    pass
```

---

### Solution 1


```python
def camel_case(string):
    return "".join([w.title() for w in string.split()])
```

---

### Solution 2


```python
def camel_case(string):
    return string.title().replace(" ", "")
```

---



[See on CodeWars.com](https://www.codewars.com/kata/587731fda577b3d1b0001196)
