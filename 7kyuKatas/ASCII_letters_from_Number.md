# CodeWars Python Solutions

---

## ASCII letters from Number


You have to create a function that converts integer given as string into ASCII uppercase letters.

All ASCII characters have their numerical order in table.

For example,

```
from ASCII table, character of number 65 is "A".
```


Numbers will be next to each other, So you have to split given number to two digit long integers.

For example,


```
'658776' to [65, 87, 76] and then turn it into 'AWL'.
```

Good Luck!

---

### Given Code


```python
def convert(number):
    pass
```

---

### Solution


```python
def convert(number):
    return "".join([chr(int(number[e:e+2])) for e in range(0,len(number),2)])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/589ebcb9926baae92e000001)
