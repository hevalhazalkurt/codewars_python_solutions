# CodeWars Python Solutions

---

## noobCode 01: SUPERSIZE ME.... or rather, this integer!

Write a function that rearranges an integer into its largest possible value.



```python
super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
```

If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.


---

### Given Code


```python
def super_size(n):
    #your code here
```

---

### Solution 1


```python
def super_size(n):
    return int("".join(sorted([x for x in str(n)], reverse=True)))
```


---

### Solution 2


```python
def super_size(n):
    return int("".join(sorted(str(n), reverse=True)))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5709bdd2f088096786000008)
