# CodeWars Python Solutions

---

## Most sales


**Description:**

You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:

- products: `["Computer", "Cell Phones", "Vacuum Cleaner"]`
- amounts: `[3, 24, 8]`
- prices: `[199, 299, 399]`

return the three product names with the highest revenue (`amount * price`).

Note: if multiple products have the same revenue, order them according to their original positions in the input list.

---

### Given Code


```python
def top3(products, amounts, prices):
    # code
```

---

### Solution


```python
def top3(products, amounts, prices):
    top = []
    for i in range(len(products)):
        top.append((amounts[i] * prices[i], products[i]))
    return [p[1] for p in sorted(top, reverse=True, key=lambda x: x[0])][:3]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5e16ffb7297fe00001114824)
