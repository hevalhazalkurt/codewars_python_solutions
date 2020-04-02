# CodeWars Python Solutions

---

## Simplify the number!

Given a positive integer as input, return the output as a string in the following format:

Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.


**Examples**

|Input	| Output |
|--|--|
| 0	| ""|
| 56 | "5*10+6" |
| 60	| "6*10" |
| 999	| "9*100+9*10+9" |
| 10004	| "1*10000+4" |

Note: `input >= 0`


---

### Given Code


```python
def simplify(number):
    pass
```

---

### Solution


```python
def simplify(number):
    number = str(number)
    if len(number) == 1:
        if number == "0":
            return ""
        else:        
            return number

    l = len(number) -1
    n = []

    for c in number[:-1]:
        if c != "0":
            n.append("{}*1{}".format(c, "0"*l))
        l -= 1

    return "+".join(n) + "+" + number[-1] if number[-1] != "0" else "+".join(n)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5800b6568f7ddad2c10000ae/)
