# CodeWars Python Solutions

---

## Basic Mathematical Operations

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Example:

```python
basic_op('+', 4, 7)         # Output: 11
basic_op('-', 15, 18)       # Output: -3
basic_op('*', 5, 5)         # Output: 25
basic_op('/', 49, 7)        # Output: 7
```


---

### Given Code


```python
def basic_op(operator, value1, value2):
    pass
```

---

### Solution


```python
def basic_op(operator, value1, value2):
    return {"+": value1 + value2, "-": value1 - value2, "*": value1 * value2, "/": value1 / value2}[operator]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/57356c55867b9b7a60000bd7/)
