# CodeWars Python Solutions

---

## Find the unique number


There is an array with some numbers. All numbers are equal except for one. Try to find it!


```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.


---

### Given Code


```python
def find_uniq(arr):
    # your code here
```

---

### Solution 1


```python
def find_uniq(arr):
    for char in set(arr):
        if arr.count(char) == 1:
            return char
```


-------

[See on CodeWars.com](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
