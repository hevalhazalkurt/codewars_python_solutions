# CodeWars Python Solutions

---

## Sums of Parts


Let us consider this example (array written in general format):

```python
ls = [0, 1, 3, 6, 10]
```

Its following parts:

```python
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
```


The corresponding sums are (put together in a list): `[20, 20, 19, 16, 10, 0]`

The function `parts_sums` (or its variants in other languages) will take as parameter a list `ls` and return a list of the sums of its parts as defined above.

**Other Examples:**

```python
ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
```

**Notes**

* Some lists can be long.
* Please ask before translating: some translations are already written and published when/if the kata is approved.



---

### Given Code


```python
def parts_sums(ls):
    pass
```

---

### Solution 1


```python
def parts_sums(ls):
    cop = list(ls)
    top = sum(ls)
    sums = 0
    parts = []
    for i in range(len(ls)):
        if len(parts) == 0:
            parts.append(top)
        else:
            parts.append(top - sums)
        sums += cop[i]
    parts.append(0)
    return parts
```

---

### Solution 2


```python
def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1]-i)
    return sums
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5ce399e0047a45001c853c2b)
