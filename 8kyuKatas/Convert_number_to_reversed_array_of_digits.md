# CodeWars Python Solutions

---

## Convert number to reversed array of digits

Given a random number you have to return the digits of this number within an array in reverse order.



**Example**

```python
348597 => [7,9,5,8,4,3]
```

---

### Given Code


```python
def digitize(n):
    return
```

---

### Solution 1


```python
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
```


---

### Solution 2


```python
def digitize(n):
    return list(map(int, str(n)))[::-1]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5583090cbe83f4fd8c000051)
