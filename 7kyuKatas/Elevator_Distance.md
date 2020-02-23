# CodeWars Python Solutions

---

## Elevator Distance

Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.

Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.


```python
# simple examples
elevatorDistance([5,2,8]) = 9
elevatorDistance([1,2,3]) = 2
elevatorDistance([7,1,7,1]) = 18

# if two consecutive floors are the same,
# distance travelled between them is 0
elevatorDistance([3,3]) = 0
```

Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.

---

### Given Code


```python
def elevator_distance(array):
    pass
```

---

### Solution 1


```python
def elevator_distance(array):
    return sum([abs(array[i] - array[i+1]) for i in range(len(array)-1)])
```


---

### Solution 2


```python
def elevator_distance(array):
    dist = 0
        for i in range(len(array)-1):
            dist += abs(array[i] - array[i+1])
        return dist
```


---


[See on CodeWars.com](https://www.codewars.com/kata/59f061773e532d0c87000d16/)
