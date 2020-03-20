# CodeWars Python Solutions

---

## Building Strings From a Hash


Complete the solution so that it takes the object (JavaScript/CoffeeScript) or hash (ruby) passed in and generates a human readable string from its key/value pairs.

The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.


**Examples**


```python
solution({"a": 1, "b": '2'}) # should return "a = 1,b = 2"
```



---

### Given Code


```python
def solution(pairs):
    pass
```

---

### Solution


```python
def solution(pairs):
    return ",".join(sorted(["{} = {}".format(k,v) for k,v in pairs.items()]))
```



---


[See on CodeWars.com](https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2)
