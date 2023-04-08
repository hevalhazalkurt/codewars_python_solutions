# CodeWars Python Solutions

---

## Fix My Phone Numbers!

### Fix My Phone Numbers
Oh thank goodness you're here! The last intern has completely ruined everything!

All of our customer's phone numbers have been scrambled, and we need those phone numbers to annoy them with endless sales calls!

### The Format
Phone numbers are stored as strings and comprise 11 digits, eg `'02078834982'` and must always start with a `0`.

However, something strange has happened and now all of the phone numbers contain lots of random characters, whitespace and some are not phone numbers at all!

For example, `'02078834982'` has somehow become `'efRFS:)0207ERGQREG88349F82!'` and there are lots more lines that we need to check.

### The Task
Given a string, you must decide whether or not it contains a valid phone number. If it does, return the corrected phone number as a string ie. `'02078834982'` with no whitespace or special characters, else return `"Not a phone number"`.

---

### Given Code


```python
def is_it_a_num(s: str) -> str:
    pass
```

---

### Solution 


```python
def is_it_a_num(s: str) -> str:
    numbers = "".join([i for i in s if i.isnumeric()])
    return numbers if numbers.startswith("0") and len(numbers) == 11 else "Not a phone number"
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/596343a24489a8b2a00000a2)
