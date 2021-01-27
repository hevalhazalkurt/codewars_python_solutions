# CodeWars Python Solutions

---

## String incrementer

Your job is to write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

**Examples:**

```
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
```


*Attention: If the number has leading zeros the amount of digits should be considered.*



---

### Given Code


```python
def increment_string(s):
    pass
```

---

### Solution


```python
import re

def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'

```


---


[See on CodeWars.com](https://www.codewars.com/kata/54a91a4883a7de5d7800009c/)
