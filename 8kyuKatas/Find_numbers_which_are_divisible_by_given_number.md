# CodeWars Python Solutions

---

## Find numbers which are divisible by given number

Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of `numbers` and the second is the `divisor`.


**Example**

```python
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
```

---

### Given Code


```python
def divisible_by(numbers, divisor):
    pass
```

---

### Solution


```python
def divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55edaba99da3a9c84000003b/)
