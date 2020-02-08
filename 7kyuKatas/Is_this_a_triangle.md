# CodeWars Python Solutions

---

## Is this a triangle?


**Definition**

Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).


---

### Given Code


```python
def is_triangle(a, b, c):
    pass
```

---

### Solution


```python
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56606694ec01347ce800001b)
