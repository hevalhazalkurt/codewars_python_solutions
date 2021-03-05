# CodeWars Python Solutions

---

## Re-organize the weapons!

The characters of Chima need your help. Their weapons got mixed up! They need you to write a program that accepts the name of a character in Chima then tells which weapon he/she owns.

For example: for the character `"Laval"` your program should return the solution `"Laval-Shado Valious"`

You must complete the following character-weapon pairs:

* Laval-Shado Valious,
* Cragger-Vengdualize,
* Lagravis-Blazeprowlor,
* Crominus-Grandorius,
* Tormak-Tygafyre,
* LiElla-Roarburn.

Return `"Not a character"` for invalid inputs.


---

### Given Code


```python
def identify_weapon(character):
    #insert your code here...FOR CHIMA!
```

---

### Solution


```python
def identify_weapon(character):
    #insert your code here...FOR CHIMA!
    weapons = {
        "Laval": "Shado Valious",
        "Cragger": "Vengdualize",
        "Lagravis": "Blazeprowlor",
        "Crominus": "Grandorius",
        "Tormak": "Tygafyre",
        "LiElla": "Roarburn"
    }
    return f"{character}-{weapons.get(character)}" if character in weapons else "Not a character"
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5470ae03304c1250b4000e57)
