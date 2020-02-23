# CodeWars Python Solutions

---

## Summing a number's digits

Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example:

```Python
sum_digits(10)  # Returns 1
sum_digits(99)  # Returns 18
sum_digits(-32) # Returns 5
```


### Given Code


```python
def sum_digits(number):
    pass
```

---

### Solution


```python
def sum_digits(number):
    return sum(int(i) for i in str(number) if i.isdigit())
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52f3149496de55aded000410/)
