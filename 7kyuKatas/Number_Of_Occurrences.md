# CodeWars Python Solutions

---

## Number Of Occurrences

Write a functionthat returns the number of occurrences of an element in an array.

**Examples**

```
sample = [0, 1, 2, 2, 3]
number_of_occurrences(0, sample) == 1
number_of_occurrences(4, sample) == 0
number_of_occurrences(2, sample) == 2
number_of_occurrences(3, sample) == 1
```

---

### Given Code


```python
def number_of_occurrences(element, sample):
    pass
```

---

### Solution


```python
def number_of_occurrences(element, sample):
    return sample.count(element)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52829c5fe08baf7edc00122b)
