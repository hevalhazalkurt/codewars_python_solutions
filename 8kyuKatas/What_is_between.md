# CodeWars Python Solutions

---

## What is between?

Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

```python
a = 1
b = 4
--> [1, 2, 3, 4]
```

---

### Given Code


```python
def between(a,b):
    pass
```

---

### Solution 


```python
def between(a,b):
    return [i for i in range(a,b+1)]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55ecd718f46fba02e5000029/)
