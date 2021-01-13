# CodeWars Python Solutions

---

## String Breakers

I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.

```python
Example:

n = 5;

st = "This is an example string";

Return value:
Thisi
sanex
ample
strin
g

Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'
```


---

### Given Code


```python
def string_breakers(n, st):
    pass
```

---

### Solution 1


```python
def string_breakers(n, st):
    new = []
    for e,i in enumerate(list(st.replace(" ", ""))):
        if e != 0 and e % n == 0:
            new.append("\n")
            new.append(i)
        else:
            new.append(i)
    return "".join(new)
```


### Solution 2


```python
def string_breakers(n, st):
    s = st.replace(" ", "")
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/59d398bb86a6fdf100000031)
