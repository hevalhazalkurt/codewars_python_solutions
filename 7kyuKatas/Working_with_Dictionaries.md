# CodeWars Python Solutions

---

## Working with Dictionaries

In this kata we have to create a function that will give us some specific information of a data base. We have a sequence of postive integers that is registered by OEIS with the code [001055](https://oeis.org/A001055). This sequence give us the amount of ways that a number may be expressed as a product of its factors (including the number itself multiplied by one.)

The first terms of this sequence are shown below:

```
n-th term    a(n)
1             1
2             1
3             1
4             2
5             1
6             2
7             1
8             3
9             2
10            2
11            1
12            4
13            1
14            2
15            2
16            5
```


In the preloaded section you are given a hash table named `A001055` (Python and JavaScript) or `$a001055` (Ruby), where keys are the numbers from `1` to `1006`, and the values are the respective terms of the aforementioned sequence.

You have to create the function that receives three arguments:

* An array with 2 elements that represent the numbers in range `[a, b]` to be considered.
* A string with five possible valid values: `"equals to"`, `"higher than"`, `"lower than"`, `"higher and equals to"`, and `"lower and equals to"` (any other value is considered invalid).
* The element of the `A001055` sequence.

The function should return the amount of numbers that fulfill our conditions and a sorted list of these numbers.


**Examples**

1. We want to know about the numbers between `10` and `21` (included) that have more than `1` multiplicative partition:

```python
range = [10, 21]
str = "higher than"
val = 1

result = (8, [10, 12, 14, 15, 16, 18, 20, 21])
```

2. We want to know the numbers between `25` and `75` that have more than or equals to `5` multiplicative partitions:

```python
range = [25, 75]
str = "higher and equals to"
val = 5

result = (13, [30, 32, 36, 40, 42, 48, 54, 56, 60, 64, 66, 70, 72])
```

If the string command is wrong, the function will return `"wrong constraint"`:

```python
range = [25, 75]
str = "qwerty"
val = 5

result = "wrong constraint"
```

Enjoy it!!





---

### Given Code


```python
def inf_database(range_, str_, val):
    global A001055
    return ()
```

---

### Solution 1


```python
import operator

def inf_database(range_, str_, val):
    global A001055
    s = {
        "higher than" : operator.gt,
        "higher and equals to": operator.ge,
        "equals to": operator.eq,
        "lower than": operator.lt,
        "lower and equals to" : operator.le}

    if str_ in s:
        l = [i for i in range(range_[0], range_[1]+1) if s[str_](A001055[i],val)]
        return (len(l), l)
    else:
        return "wrong constraint"
```


### Solution 2


```python

def inf_database(range_, str_, val):
    global A001055
    s = {
        "higher than" : lambda a,b: a>b,
        "higher and equals to": lambda a,b: a>=b,
        "equals to": lambda a,b: a==b,
        "lower than": lambda a,b: a<b,
        "lower and equals to" : lambda a,b: a<=b}

    if str_ in s:
        l = [i for i in range(range_[0], range_[1]+1) if s[str_](A001055[i],val)]
        return (len(l), l)
    else:
        return "wrong constraint"
```


### Solution 3


```python

def inf_database(range_, str_, val):
    global A001055
    s = {
        "higher than" : int.__gt__,
        "higher and equals to": int.__ge__,
        "equals to": int.__eq__,
        "lower than": int.__lt__,
        "lower and equals to" : int.__le__}

    if str_ in s:
        l = [i for i in range(range_[0], range_[1]+1) if s[str_](A001055[i],val)]
        return (len(l), l)
    else:
        return "wrong constraint"
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5639302a802494696d000077)
