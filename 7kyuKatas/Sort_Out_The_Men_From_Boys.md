# CodeWars Python Solutions

---

## Sort Out The Men From Boys

**Scenario**

Now that the competition gets tough it will Sort out the men from the boys .

Men are the Even numbers and Boys are the odd


<br>


**Task**

Given an array/list `[]` of `n` integers , Separate The even numbers from the odds , or Separate the men from the boys

<br>

**Notes**

* Return an array/list where Even numbers come first then odds
* Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
* Array/list size is at least `*4*** `.
* Array/list numbers could be a mixture of positives , negatives .
* Have no fear , It is guaranteed that no Zeroes will exists .
* Repetition of numbers in the array/list could occur , So (duplications are not included when separating).


<br>

**Input >> Output Examples:**

```python
menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3})
```

*Explanation:*

Since , `{ 14 }` is the even number here , So it came first , then the odds in descending order `{17 , 7 , 3}`.

```python
menFromBoys ({-94, -99 , -100 , -99 , -96 , -99 }) ==> return ({-100 , -96 , -94 , -99})
```

*Explanation:*

- Since , `{ -100, -96 , -94 } `is the even numbers here , So it came first in ascending order , then the odds in descending order `{ -99 }`
- Since , (Duplications are not included when separating) , then you can see only one `(-99)` was appeared in the final array/list .

```python
menFromBoys ({49 , 818 , -282 , 900 , 928 , 281 , -282 , -1 }) ==> return ({-282 , 818 , 900 , 928 , 281 , 49 , -1})
```

*Explanation:*

- Since , `{-282 , 818 , 900 , 928 }` is the even numbers here , So it came first in ascending order , then the odds in descending order `{ 281 , 49 , -1 }`
- Since , (Duplications are not included when separating) , then you can see only one `(-282)` was appeared in the final array/list .



---

### Given Code


```python
def men_from_boys(arr):
    pass
```

---

### Solution 1


```python
def men_from_boys(arr):
    return sorted([i for i in set(arr) if i % 2 == 0]) + sorted([i for i in set(arr) if i % 2 != 0], reverse=True)
```


---

### Solution 2


```python
def men_from_boys(arr):
    return sorted(set(arr), key=lambda n: (n%2, n * (-1)**(n%2)))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5af15a37de4c7f223e00012d/)
