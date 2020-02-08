# CodeWars Python Solutions

---

## Highest and Lowest


**Definition**

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.



**Example**

```Python
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```


**Notes**

- All numbers are valid `Int32`, no need to validate them.
- There will always be at least one number in the input string.
- Output string must be two numbers separated by a single space, and highest number is first.


---

### Given Code


```python
def high_and_low(numbers):
    pass
```

---

### Solution


```python
def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return " ".join([str(max(nums)), str(min(nums))])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/554b4ac871d6813a03000035)
