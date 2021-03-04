# CodeWars Python Solutions

---

## Thinkful - Dictionary drills: Order filler

You're running an online business and a big part of your day is fulfilling orders. As your volume picks up that's been taking more of your time, and unfortunately lately you've been running into situations where you take an order but can't fulfill it.

You've decided to write a function `fillable()` that takes three arguments: a dictionary `stock` representing all the merchandise you have in stock, a string `merch` representing the thing your customer wants to buy, and an integer n representing the number of units of merch they would like to buy. Your function should return `True` if you have the merchandise in stock to complete the sale, otherwise it should return `False`.

Valid data will always be passed in and `n` will always be `>= 1`.


---

### Given Code


```python
def fillable(stock, merch, n):
    pass
```

---

### Solution


```python
def fillable(stock, merch, n):
    return True if merch in stock and stock[merch] >= n else False
```



---


[See on CodeWars.com](https://www.codewars.com/kata/586ee462d0982081bf001f07)
