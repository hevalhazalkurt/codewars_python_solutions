# CodeWars Python Solutions

---

## Player Contact Manager


You are the Dungeon Master for a public DnD game at your local comic shop and recently you've had some trouble keeping your players' info neat and organized so you've decided to write a bit of code to help keep them sorted!

The goal of this code is to create an array of objects that stores a player's name and contact number from a given string.

The method should return an empty array if the argument passed is an empty string or `nil`/`None`/`null`.


**Examples**


```python
player_manager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{"player": "John Doe", "contact": 8167238327}, {"player": "Jane Doe", "contact": 8163723827}]
player_manager(None) returns []
player_manager("")   returns []
```

Have at thee!

---

### Given Code


```python
def player_manager(players):
    pass
```

---

### Solution


```python
def player_manager(players):
    contacts = []
    if players:
        for e,i in enumerate(players.split(", ")):
            if e % 2 == 0:
                temp = {}
                temp["contact"] = int(players.split(", ")[e+1])
                temp["player"] = i
                contacts.append(temp)
        return contacts
    else:
        return []
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5b203de891c7469b520000b4)
