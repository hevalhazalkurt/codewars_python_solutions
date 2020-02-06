# CodeWars Python Solutions

---

## Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because `1^2 + 2^2 + 2^2 = 9`.

---

### Given Code


```python
def square_sum(numbers):
    #your code here
```

---

### Solution


```python
def square_sum(numbers):
    return sum([num*num for num in numbers])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/515e271a311df0350d00000f)
