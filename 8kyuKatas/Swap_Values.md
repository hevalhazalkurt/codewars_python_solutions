# CodeWars Python Solutions

---

## Swap Values

I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?

---

### Given Code


```python
def swap_values(args):
    args[0] = args[1]
    args[1] = args[0]
```

---

### Solution 1


```python
def swap_values(args):
    temp = args[0]
    args[0] = args[1]
    args[1] = temp
    return args
```


---

### Solution 2


```python
def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/)
