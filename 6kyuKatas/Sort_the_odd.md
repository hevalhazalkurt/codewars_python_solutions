# CodeWars Python Solutions

---

## Sort the odd


**Definition**

You have an array of numbers.

Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example :

```python
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
```

NOTE: All numbers will be whole numbers greater than 0.

---

### Given Code


```python
def sort_array(source_array):
    pass
```

---

### Solution


```python
def sort_array(source_array):
    odds = sorted([n for n in source_array if n % 2 != 0])
    for n in source_array:
        if n % 2 == 0:
            odds.insert(source_array.index(n), n)
    return odds
```

---


[See on CodeWars.com](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)
