# CodeWars Python Solutions

---

## Colour Association


Colour plays an important role in our lifes. Most of us like this colour better then another. User experience specialists believe that certain colours have certain psychological meanings for us.

You are given a 2D array, composed of a colour and its 'common' association in each array element. The function you will write needs to return the colour as 'key' and association as its 'value'.

For example :


```python
var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]
```



---

### Given Code


```python
def colour_association(arr):
    pass
```

---

### Solution


```python
def colour_association(arr):
    return [{i[0]: i[1]} for i in arr]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56d6b7e43e8186c228000637)
