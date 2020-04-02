# CodeWars Python Solutions

---

## Polish alphabet

There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

Your task is to change the letters with diacritics:


```
ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
```


and print out the string without the use of the Polish letters.

Example:

```python
Input: "Jędrzej Błądziński"
```

```python
Output: "Jedrzej Bladzinski"
```

---

### Given Code


```python
def correct_polish_letters(st):
    pass
```

---

### Solution


```python
def correct_polish_letters(st):
    pol = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
    return "".join([pol[c] if c in pol else c for c in st])
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57ab2d6072292dbf7c000039/)
