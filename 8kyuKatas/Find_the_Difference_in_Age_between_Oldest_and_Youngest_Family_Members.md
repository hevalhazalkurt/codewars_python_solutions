# CodeWars Python Solutions

---

## Find the Difference in Age between Oldest and Youngest Family Members


At the annual family gathering, the family likes to find the oldest living family member’s age and the youngest family member’s age and calculate the difference between them.

You will be given an array of all the family members' ages, in any order. The ages will be given in whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0. Return a new array with [youngest age, oldest age, difference between the youngest and oldest age].


---

### Given Code


```python
def difference_in_ages(ages):
    pass
```

---

### Solution


```python
def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5720a1cb65a504fdff0003e2)
