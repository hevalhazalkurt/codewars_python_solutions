# CodeWars Python Solutions

---

## Calculate Meal Total

Create a function that returns the total of a meal including tip and tax. You should not tip on the tax.

You will be given the subtotal, the tax as a percentage and the tip as a percentage. Please round your result to two decimal places.


### Given Code


```python
def calculate_total(subtotal, tax, tip):
    pass
```

---

### Solution


```python
def calculate_total(subtotal, tax, tip):
    return round(sum([subtotal, subtotal*tax/100, subtotal*tip/100]), 2)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/58545549b45c01ccab00058c/)
