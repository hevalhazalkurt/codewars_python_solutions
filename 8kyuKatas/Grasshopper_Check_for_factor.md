# CodeWars Python Solutions

---

## Grasshopper - Check for factor


**Description:**

This function should test if the `factor` is a factor of `base`.

Return `true` if it is a factor or `false` if it is not.


**About factors**

Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: `2 * 3 = 6`

- You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
- You can use the mod operator (`%`) in most languages to check for a remainder

For example 2 is not a factor of 7 because: `7 % 2 = 1`

Note: `base` is non-negative number and `factor` is positive number.



---

### Given Code


```python
def check_for_factor(base, factor):
    pass
```

---

### Solution


```python
def check_for_factor(base, factor):
    return base % factor == 0
```

---


[See on CodeWars.com](https://www.codewars.com/kata/55cbc3586671f6aa070000fb)
