# CodeWars Python Solutions

---

## Count characters in your string

The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this `aba` then the result should be `{ 'a': 2, 'b': 1 }`

What if the string is empty ? Then the result should be empty object literal `{ }`

For C#: Use a `Dictionary<char, int>` for this kata!

---

### Given Code


```python
def count(string):
    pass
```

---

### Solution


```python
def count(string):
    return {c:string.count(c) for c in string}
```

---


[See on CodeWars.com](https://www.codewars.com/kata/52efefcbcdf57161d4000091/)
