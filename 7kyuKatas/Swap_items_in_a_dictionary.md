# CodeWars Python Solutions

---

## Swap items in a dictionary

In this kata, you will take the keys and values of a dictionary and swap them around.

You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old keys as values under their original keys.

For example, given the dictionary: `{'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}`,

you should return: `{'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}`

**Notes:**

* The dictionary given will only contain strings
* The dictionary given will not be empty
* You do not have to sort the items in the lists


---

### Given Code


```python
def switch_dict(dic):
    pass
```

---

### Solution


```python
def switch_dict(dic):
    new = {}
    for k,v in dic.items():
        if v in new:
            new[v] = new[v] + [k]
        else:
            new[v] = [k]
    return new
```



---


[See on CodeWars.com](https://www.codewars.com/kata/5a21e090f28b824def00013c)
