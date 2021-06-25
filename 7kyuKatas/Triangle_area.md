# CodeWars Python Solutions

---

## Triangle area

Calculate area of given triangle. Create a function t_area that will take a string which will represent triangle, find area of the triangle, one space will be equal to one length unit. The smallest triangle will have one length unit.

Hints

Ignore dots.

Example:

.
.      .  
.      .       .      ---> should return 2.0

.
.      .  
.      .       .     
.      .       .      .      ---> should return 4.5


---

### Given Code


```python
def t_area(t_str):
    pass
```

---

### Solution 1


```python
def t_area(t_str):
    tri = t_str.split("\n")
    a = (len(tri)-2) - 1
    b = tri[-2].count(".") - 1
    return (a*b) / 2
```

---

### Solution 2


```python
def t_area(t_str):
    return (t_str.count('\n') - 2) ** 2 /2
```



---


[See on CodeWars.com](https://www.codewars.com/kata/59bd84b8a0640e7c49002398)
