# CodeWars Python Solutions

---

## Removing Elements


Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.

**Example**

```python
my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
```

None of the arrays will be empty, so you don't have to worry about that!


---

### Given Code


```python
def remove_every_other(my_list):
    pass
```

---

### Solution 1


```python
def remove_every_other(my_list):
    return [i for e,i in enumerate(my_list) if e % 2 == 0]
```

---

### Solution 2


```python
def remove_every_other(my_list):
    return my_list[::2]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5769b3802ae6f8e4890009d2)
