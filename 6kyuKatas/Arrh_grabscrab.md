# CodeWars Python Solutions

---

## Arrh, grabscrab!


**Definition**

Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.


**Example**

```
grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
```

Should return `["sport", "ports"]`.

Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

Good luck!

---

### Given Code


```python
def grabscrab(word, possible_words):
    pass
```

---

### Solution 1


```python
def grabscrab(word, possible_words):
    words = []
    letters1 = {l:word.count(l) for l in word}
    for word in possible_words:
        letters2 = {l:word.count(l) for l in word}
        if letters1 == letters2:
            words.append(word)
    return words
```

---

### Solution 2


```python
def grabscrab(word, possible_words):
    return [w for w in possible_words if sorted(word) == sorted(w)]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52b305bec65ea40fe90007a7)
