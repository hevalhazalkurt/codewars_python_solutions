# CodeWars Python Solutions

---

## Summy

Write a function that takes a string which has integers inside it separated by spaces, and your task is to convert each integer in the string into an integer and return their sum.

**Example**

```python
summy("1 2 3")  ==> 6
```

Good luck!

---

### Given Code


```python
def summy(string_of_ints):
    pass
```

---

### Solution


```python
def summy(string_of_ints):
    return sum([int(i) for i in string_of_ints.split(" ")])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/599c20626bd8795ce900001d)
