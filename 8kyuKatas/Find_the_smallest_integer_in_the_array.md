# CodeWars Python Solutions

---

## Find the smallest integer in the array

Given an array of integers your solution should find the smallest integer.

For example:

* Given `[34, 15, 88, 2]` your solution will return `2`
* Given `[34, -345, -1, 100]` your solution will return `-345`

You can assume, for the purpose of this kata, that the supplied array will not be empty.

---

### Given Code


```python
def find_smallest_int(arr):
    # Code here
```

---


### Solution 1


```python
def find_smallest_int(arr):
    return min(arr)
```

---

### Solution 2


```python
def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
```

---


[See on CodeWars.com](https://www.codewars.com/kata/55a2d7ebe362935a210000b2)
