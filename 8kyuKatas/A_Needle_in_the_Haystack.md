# CodeWars Python Solutions

---

## A Needle in the Haystack


**Definition**

Can you find the needle in the haystack?

Write a function `findNeedle()` that takes an `array` full of junk but containing one `"needle"`

After your function finds the needle it should return a message (as a string) that says:

`"found the needle at position "` plus the `index` it found the needle, so:


```Python
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
```

should return `"found the needle at position 5"`

---

### Given Code


```python
def find_needle(haystack):
    pass
```

---

### Solution


```python
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c)
