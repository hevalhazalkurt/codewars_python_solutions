# CodeWars Python Solutions

---

## Row Weights

**Scenario**

Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

<br>

**Task**

Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

<br>

**Notes**

* Array size is at least 1.
* All numbers will be positive.

<br>

**Input >> Output Examples**

```python
rowWeights([13, 27, 49])  ==>  return (62, 27)
```

***Explanation:***

The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

<br>

```python
rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
```

***Explanation:***

The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.


<br>

```python
rowWeights([80])  ==>  return (80, 0)
```

***Explanation:***

The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.

---

### Given Code


```python
def row_weights(array):
    pass
```

---

### Solution 1


```python
def row_weights(array):
    return sum([i for e,i in enumerate(array) if e % 2 == 0]), sum([i for e,i in enumerate(array) if e % 2 != 0])
```


---

### Solution 2


```python
def row_weights(array):
    return sum(array[::2]), sum(array[1::2])
```


---

### Solution 3


```python
def row_weights(array):
    first = 0
    second = 0
    for e,i in enumerate(array):
        if e % 2 == 0:
            first += i
        else:
            second += i
    return first, second
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/)
