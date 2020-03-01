# CodeWars Python Solutions

---

## How much will you spend?

Given a dictionary of items and their costs and a array specifying the items bought, calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.


```python
costs = {'socks':5, 'shoes':60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 = 65
#-> 65 + 0.09 of 65 = 70.85
#-> Output: 70.85
```

---

### Given Code


```python
def getTotal(costs, items, tax):
    pass
```

---

### Solution


```python
def getTotal(costs, items, tax):
    return round(sum([costs[i] for i in items if i in costs]) * (1 + tax), 2)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/585d7b4685151614190001fd/)
