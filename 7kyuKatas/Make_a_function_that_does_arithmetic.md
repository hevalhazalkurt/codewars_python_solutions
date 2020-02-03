# CodeWars Python Solutions

---

## Make a function that does arithmetic!

Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

`a` and `b` will both be positive integers, and `a` will always be the first number in the operation, and `b` always the second.

The four operators are `"add"`, `"subtract"`, `"divide"`, `"multiply"`.

Try to do it without using if statements!

A few examples:

```
arithmetic(5, 2, "add")      => returns 7
arithmetic(5, 2, "subtract") => returns 3
arithmetic(5, 2, "multiply") => returns 10
arithmetic(5, 2, "divide")   => returns 2.5
```

---

### Given Code


```python
def arithmetic(a, b, operator):
    # your code here
```

---

### Solution


```python
def arithmetic(a, b, operator):
    ops = {"add": a+b, "subtract": a-b, "multiply":a*b, "divide":a/b}
    return ops[operator]
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/583f158ea20cfcbeb400000a)
