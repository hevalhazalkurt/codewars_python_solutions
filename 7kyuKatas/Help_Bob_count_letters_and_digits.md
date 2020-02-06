# CodeWars Python Solutions

---

## Help Bob count letters and digits

Bob is a lazy man.

He needs you to create a method that can determine how many letters and digits are in a given string.

**Example:**

```
"hel2!lo" --> 6
"wicked .. !" --> 6
"!?..A" --> 1
```

---

### Given Code


```python
def count_letters_and_digits(s):
    pass
```

---

### Solution


```python
def count_letters_and_digits(s):
    return len([char for char in s if char.isdigit() or char.isalpha()])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5738f5ea9545204cec000155)
