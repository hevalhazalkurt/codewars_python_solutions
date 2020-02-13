# CodeWars Python Solutions

---

## Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

```
double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
```



---

### Given Code


```python
def double_char(s):
    pass
```

---

### Solution


```python
def double_char(s):
    return "".join([c * 2 for c in s])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56b1f01c247c01db92000076)
