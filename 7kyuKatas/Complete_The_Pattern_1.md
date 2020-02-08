# CodeWars Python Solutions

---

## Complete The Pattern # 1


**Task:**

You have to write a function `pattern` which returns the following Pattern (See Pattern & Examples) up to `n` number of rows.

Note: Returning the pattern is not the same as Printing the pattern.


**Rules/Note:**

- If `n < 1` then it should return `""` i.e. empty string.
- There are no whitespaces in the pattern.

**Pattern**

```
1
22
333
....
.....
nnnnnn
```


**Examples**

- `pattern(5)`

```
1
22
333
4444
55555
```


- `pattern(11)`

```
1
22
333
4444
55555
666666
7777777
88888888
999999999
10101010101010101010
1111111111111111111111
```


***Hint: Use \n in string to jump to next line***

---

### Given Code


```python
def pattern(n):
    # Happy Coding ^_^
```

---

### Solution


```python
def pattern(n):
    return "\n".join([str(i)*i for i in range(1, n+1)])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5572f7c346eb58ae9c000047)
