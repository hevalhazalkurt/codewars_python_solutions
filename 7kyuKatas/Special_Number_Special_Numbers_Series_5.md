# CodeWars Python Solutions

---

## Special Number (Special Numbers Series #5 )

**Definitiion**

A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .


**Notes**

- The number passed will be positive (N > 0) .
- All single-digit numbers with in the interval [0:5] are considered as special number.



**Input >> Output Examples**

```python
specialNumber(2) ==> return "Special!!"
```

It's a single-digit number within the interval [0:5] .



```python
specialNumber(9) ==> return "NOT!!"
```

Although, it's a single-digit number but Outside the interval [0:5] .


```python
specialNumber(23) ==> return "Special!!"
```

All the number's digits formed from the interval [0:5] digits .


```python
specialNumber(39) ==> return "NOT!!"
```

Although, there is a digit (3) Within the interval But the second digit is not (Must be ALL The Number's Digits ) .

```python
specialNumber(59) ==> return "NOT!!"
```

Although, there is a digit (5) Within the interval But the second digit is not (Must be ALL The Number's Digits ) .


```python
specialNumber(513) ==> return "Special!!"
specialNumber(709) ==> return "NOT!!"
```


---

### Given Code


```python
def special_number(number):
    pass
```

---

### Solution 1


```python
def special_number(number):
    return "Special!!" if len([True for x in str(number) if int(x) < 6]) == len(str(number)) else "NOT!!"
```


---

### Solution 2


```python
def special_number(number):
    return "Special!!" if max(str(number)) <= "5" else "NOT!!"
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5a55f04be6be383a50000187)
