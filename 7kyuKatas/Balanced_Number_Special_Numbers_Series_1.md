# CodeWars Python Solutions

---

## Balanced Number (Special Numbers Series # 1)

**Definition**

Balanced number is the number that The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal.


**Task**

Given a number, Find if it is `Balanced` or not .


Warm-up (Highly recommended) : [Playing With Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

**Notes**

- If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0
- The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g 413023 is a balanced number because the left sum and right sum are both 5.
- Number passed is always Positive .
- Return the result as String


**Input >> Output Examples**

```python
(balanced-num 7) ==> return "Balanced"
```

***Explanation:***

- Since , The sum of all digits to the left of the middle digit (0)
- and the sum of all digits to the right of the middle digit (0) are equal , then It's Balanced


```python
(balanced-num 295591) ==> return "Not Balanced"
```

***Explanation:***

- Since , The sum of all digits to the left of the middle digits (11)
- and the sum of all digits to the right of the middle digits (10) are Not equal , then It's Not Balanced
- Note : The middle digit(s) are 55 .


```python
(balanced-num 959) ==> return "Balanced"
```

***Explanation:***

- Since , The sum of all digits to the left of the middle digits (9)
- and the sum of all digits to the right of the middle digits (9) are equal , then It's Balanced
- Note : The middle digit is 5 .

```python
(balanced-num 27102983) ==> return "Not Balanced"
```

***Explanation:***

- Since , The sum of all digits to the left of the middle digits (10)
- and the sum of all digits to the right of the middle digits (20) are Not equal , then It's Not Balanced
- Note : The middle digit(s) are 02 .



---

### Given Code


```python
def balanced_num(number):
    pass
```

---

### Solution 1


```python
def balanced_num(number):
    nums = [int(n) for n in str(number)]
    if len(nums) <= 2:
        return "Balanced"
    elif len(nums) % 2 == 0:
        if sum(nums[:len(nums)//2-1]) == sum(nums[len(nums)//2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        if sum(nums[:len(nums)//2]) == sum(nums[len(nums)//2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"
```

---

### Solution 2


```python
def balanced_num(number):
    return '%sBalanced' % ( 'Not ' if (sum(int(e) for e in str(number)[:(len(str(number))+1)//2-1]) !=  sum(int(e) for e in str(number)[(len(str(number)))//2+1:])) else '' )
```


---

### Solution 3


```python
def balanced_num(number):
    s = str(n)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5a4e3782880385ba68000018)
