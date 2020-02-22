# CodeWars Python Solutions

---

## Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:


```
name + " plays banjo"
name + " does not play banjo"
```

Names given are always valid strings.


---

### Given Code


```python
def areYouPlayingBanjo(name):
    pass
```

---

### Solution


```python
def areYouPlayingBanjo(name):
    return "{} plays banjo".format(name) if name.startswith("R") or name.startswith("r") else "{} does not play banjo".format(name)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53af2b8861023f1d88000832/)
