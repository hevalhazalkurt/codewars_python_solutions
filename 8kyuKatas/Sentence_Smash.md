# CodeWars Python Solutions

---

## Sentence Smash

Write a method `smash` that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!


**Example**

```python
words = ['hello', 'world', 'this', 'is', 'great']
smash(words) # returns "hello world this is great"
```

**Assumptions**

- You can assume that you are only given words.
- You cannot assume the size of the array.
- You can assume that you will always get an array.


**What We're Testing**

We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.


**Disclaimer**

This is for beginners so we want to test basic loops and string manipulation. Advanced users should easily be able to do this in one line.

---

### Given Code


```python
def smash(words):
    pass
```

---

### Solution


```python
def smash(words):
    return " ".join(words) if len(words) >= 1 else ""
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53dc23c68a0c93699800041d/)
