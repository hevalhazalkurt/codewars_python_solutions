# CodeWars Python Solutions

---

## Where my anagrams at?


**Definition**

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:


```python
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```python
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```



---

### Given Code


```python
def anagrams(word, words):
    pass
```

---

### Solution 1


```python
def anagrams(word, words):
    return [i for i in words if set(i) == set(word) and len(i) == len(word)]
```


---

### Solution 2


```python
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)
