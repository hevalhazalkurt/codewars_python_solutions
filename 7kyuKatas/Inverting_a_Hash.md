# CodeWars Python Solutions

---

## Inverting a Hash


**Summary**

Given a Hash made up of keys and values, invert the hash by swapping them.


**Examples**


```python
Given:

  { 'a' : 1,
    'b' : 2,
    'c' : 3 }

Return:

  { 1 : 'a',
    2 : 'b',
    3 : 'c' }



Given:

  { 'foo'   : 'bar',
    'hello' : 'world' }

Return:

  { 'bar'   : 'foo',
    'world' : 'hello' }
```

**Notes**

* Keys and values may be of any type appropriate for use as a key.
* All hashes provided as input will have unique values, so the inversion is [involutive](https://en.wikipedia.org/wiki/Involution_%28mathematics%29). In other words, do not worry about identical values stored under different keys.


---

### Given Code


```python
def invert_hash(dictionary):
    pass
```

---

### Solution


```python
def invert_hash(dictionary):
    return {v:k for k,v in dictionary.items()}
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5b5604e26dc79e6832000101)
