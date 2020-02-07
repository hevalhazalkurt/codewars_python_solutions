# CodeWars Python Solutions

---

## Century From Year

**Introduction**

The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.


**Task :**

Given a year, return the century it is in.


**Input , Output Examples** :

```python
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
```

---

### Given Code


```python
def century(year):
    # Finish this :)
    return
```

---

### Solution 1


```python
def century(year):
    return (year + 99) // 100
```


---

### Solution 2


```python
def century(year):
    if year < 1000:
        return year // 100 + 1
    elif year >= 1000 and year % 100 == 0:
        return year / 100
    else:
        return year // 100 + 1
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097)
