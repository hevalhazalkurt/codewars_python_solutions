# CodeWars Python Solutions

---

## Parse nice int from char problem


**Instructions**

Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.

---

### Given Code


```python
def get_age(age):
    pass
```

---

### Solution


```python
def get_age(age):
    return int("".join([i for i in age if i.isdigit()]))
```

---


[See on CodeWars.com](https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1)
