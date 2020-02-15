# CodeWars Python Solutions

---

## Correct the mistakes of the character recognition software

Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

- `S` is misinterpreted as `5`
- `O` is misinterpreted as `0`
- `I` is misinterpreted as `1`

The test cases contain numbers only by mistake.


---

### Given Code


```python
def correct(string):
    pass
```

---

### Solution 1


```python
def correct(string):
    mis = {"0":"O", "5":"S", "1":"I"}
    for c in string:
        if c in mis:
            string = string.replace(c, mis[c])
    return string
```

---

### Solution 2


```python
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))
```

---

### Solution 3


```python
def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')
```



---


[See on CodeWars.com](https://www.codewars.com/kata/577bd026df78c19bca0002c0)
