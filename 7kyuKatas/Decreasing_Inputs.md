# CodeWars Python Solutions

---

## Decreasing Inputs

This kata is all about adding numbers.

You will create a function named add. It will return the sum of all the arguments. Sounds easy, doesn't it?

Well Here's the Twist. The inputs will gradually decrease with their index as parameter to the function.


```python
add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
```

Remember the function will return 0 if no arguments are passed and it must round the result if sum is a float.

Example

```python
add() #=> 0
add(1,2,3) #=> 3
add(1,4,-6,20) #=> 6
```

---

### Given Code


```python
def add(*args):
    pass
```

---

### Solution


```python
def add(*args):
    return round(sum([e/i for i,e in enumerate(args, start=1)]))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/555de49a04b7d1c13c00000e/)
