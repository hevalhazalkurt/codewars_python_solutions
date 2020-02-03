# CodeWars Python Solutions

---

## Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.


**Example**

```python
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```

---

### Given Code


```python
def is_isogram(string):
    # your code here
```

---

### Solution 1


```python
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```

---

### Solution 2


```python
def is_isogram(string):
    string = string.lower()
    letters = {letter: string.count(letter) for letter in string}
    if set(letters.values()) == {1} or set(letters.values()) == set():
        return True
    else:
        return False
```

-------

[See on CodeWars.com](https://www.codewars.com/kata/54ba84be607a92aa900000f1)
