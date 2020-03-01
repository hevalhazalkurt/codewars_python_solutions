# CodeWars Python Solutions

---

## Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples:

```python
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```


---

### Given Code


```python
def to_camel_case(text):
    pass
```

---

### Solution 1


```python
def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()
    return "".join([w.capitalize() if w != words[0] else w for w in words])
```


---

### Solution 2


```python
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
```


---


[See on CodeWars.com](https://www.codewars.com/kata/517abf86da9663f1d2000003/)
