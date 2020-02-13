# CodeWars Python Solutions

---

## Anagram Detection

An anagram is the result of rearranging the letters of a word to produce a new word (see [wikipedia](https://en.wikipedia.org/wiki/Anagram)).

Note: anagrams are case insensitive

Complete the function to return `true` if the two arguments given are anagrams of each other; return `false` otherwise.


**Examples**


- `"foefet"` is an anagram of `"toffee"`
- `"Buckethead"` is an anagram of `"DeathCubeK"`


---

### Given Code


```python
def is_anagram(test, original):
    pass
```

---

### Solution 1


```python
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)
```

---

### Solution 2


```python
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
```



---


[See on CodeWars.com](https://www.codewars.com/kata/529eef7a9194e0cbc1000255)
