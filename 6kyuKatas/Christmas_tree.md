# CodeWars Python Solutions

---

## Christmas tree

Create a function that returns a christmas tree of the correct height.

For example:

`height = 5` should return:

```
    *    
   ***   
  *****  
 *******
*********
```

Height passed is always an integer between 0 and 100.

Use `\n` for newlines between each line.

Pad with spaces so each line is the same length. The last line having only stars, no spaces.

---

### Given Code


```python
def christmas_tree(height):
    pass
```

---

### Solution


```python
def christmas_tree(height):
    stars = [i for i in range(1, height*2+1, 2)]
    tree = "\n".join([("*"*star).center(stars[-1]) for star in stars])
    return tree
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52755006cc238fcae70000ed/)
