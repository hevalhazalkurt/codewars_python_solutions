# CodeWars Python Solutions

---

## Format a string of names like 'Bart, Lisa & Maggie'

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:


```python
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
```

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

---

### Given Code


```python
def namelist(names):
    pass
```

---

### Solution


```python
def namelist(names):
    if len(names) == 0 : return ""
    elif len(names) == 1 : return names[0]['name']
    else : return ", ".join([names[i]['name'] for i in range(len(names)-1)]) + " & " + names[-1]['name']
```

---


[See on CodeWars.com](https://www.codewars.com/kata/53368a47e38700bd8300030d/)
