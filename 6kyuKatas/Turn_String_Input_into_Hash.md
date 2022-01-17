# CodeWars Python Solutions

---

## Turn String Input into Hash


Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.

```python
"a=1, b=2, c=3, d=4"
```


This string should return a hash that looks like

```python
{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

### Given Code


```python
def str_to_hash(st):
    # your code here
    pass
```

---

### Solution


```python
def str_to_hash(st):
    return {i[0]:int(i[1]) for i in [item.split("=") for item in st.split(", ")]} if len(st) > 0 else {}
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52180ce6f626d55cf8000071)
