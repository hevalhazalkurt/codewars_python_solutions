# CodeWars Python Solutions

---

## Parts of a list

Write a function `partlist` that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

* Each two non empty parts will be in a pair (or an array for languages without tuples or a `struct` in C - C: see Examples test Cases - )
* Each part will be in a string
* Elements of a pair must be in the same order as in the original array.

Examples of returns in different languages:

```
a = ["az", "toto", "picaro", "zone", "kiwi"] -->
[["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"], ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]]
or
 a = {"az", "toto", "picaro", "zone", "kiwi"} -->
{{"az", "toto picaro zone kiwi"}, {"az toto", "picaro zone kiwi"}, {"az toto picaro", "zone kiwi"}, {"az toto picaro zone", "kiwi"}}
or
a = ["az", "toto", "picaro", "zone", "kiwi"] -->
[("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
or
a = [|"az", "toto", "picaro", "zone", "kiwi"|] -->
[("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
or
a = ["az", "toto", "picaro", "zone", "kiwi"] -->
"(az, toto picaro zone kiwi)(az toto, picaro zone kiwi)(az toto picaro, zone kiwi)(az toto picaro zone, kiwi)"
```

Note

You can see other examples for each language in "Your test cases"

---

### Given Code


```python
def partlist(arr):
    pass
```

---

### Solution 1


```python
def partlist(arr):
    tuples = []
    for e,i in enumerate(arr):
        if e == len(arr)-1:
            break
        else:
            tuples.append((" ".join(arr[:e+1]), " ".join(arr[e+1:])))
    return tuples
```


### Solution 2


```python
def partlist(arr):
    return [(" ".join(arr[:i]), " ".join(arr[i:])) for i in range(1, len(arr))]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56f3a1e899b386da78000732)
