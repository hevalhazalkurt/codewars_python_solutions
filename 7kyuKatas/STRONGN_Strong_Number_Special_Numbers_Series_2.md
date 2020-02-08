# CodeWars Python Solutions

---

## STRONGN Strong Number (Special Numbers Series # 2)


**Definition**

Strong number is the number that the sum of the factorial of its digits is equal to number itself.


For example: 145, since

```
1! + 4! + 5! = 1 + 24 + 120 = 145
```

So, 145 is a Strong number.

**Task**

Given a number, Find if it is Strong or not.


**Notes**

- Number passed is always Positive.
- Return the result as String


**Input >> Output Examples**

```
strong_num(1) ==> return "STRONG!!!!"
```

Since , the sum of its digits' factorial of (`1`) is equal to number itself (`1`) , Then its a Strong .

```
strong_num(123) ==> return "Not Strong !!"
```

Since the sum of its digits' factorial of `1! + 2! + 3! = 9` is not equal to number itself (`123`) , Then it's Not Strong .

```
strong_num(2)  ==>  return "STRONG!!!!"
```

Since the sum of its digits' factorial of `2! = 2` is equal to number itself (`2`) , Then its a Strong .

```
strong_num(150) ==> return "Not Strong !!"
```

Since the sum of its digits' factorial of `1! + 5! + 0! = 122` is not equal to number itself (`150`), Then it's Not Strong .

---

### Given Code


```python
def strong_num(number):
    pass
```

---

### Solution


```python
def strong_num(number):
    nums = []
    for n in str(number):
        tot = 1
        for i in range(1,int(n)+1):
            tot *= i
        nums.append(tot)
    return "STRONG!!!!" if number == sum(nums) else "Not Strong !!"
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5a4d303f880385399b000001)
