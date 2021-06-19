# CodeWars Python Solutions

---

## Which triangle is that?

Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.

It has to return a string with the type of triangle.


**Examples**


```Python
type_of_triangle(2, 2, 1) --> "Isosceles"
```


---

### Given Code


```python
def type_of_triangle(a, b, c):
    # your code here
    pass
```

---

### Solution


```python
def type_of_triangle(a, b, c):
    tup = (a,b,c)

    triangle = {1: "Equilateral",
                2: "Isosceles",
                3: "Scalene"}

    if all(isinstance(n, int) for n in tup) and (a+b)>c and (b+c)>a and (a+c)>b:
        msg = triangle.get(len(set(tup)))
    else:
        msg = "Not a valid triangle"

    return msg
```

---


[See on CodeWars.com](https://www.codewars.com/kata/564d398e2ecf66cec00000a9)
