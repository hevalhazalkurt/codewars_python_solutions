# CodeWars Python Solutions

---

## The Vowel Code

**Task**

Step 1: Create a function called `encode()` to replace all the lowercase vowels in a given string with numbers according to the following pattern:

```
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
```

For example, `encode("hello")` would return `"h2ll4"`. There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called `decode()` to turn the numbers back into vowels according to the same pattern shown above.

For example, `decode("h3 th2r2")` would return `"hi there"`.

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

<br>

---

### Given Code


```python
def encode(st):
    pass

def decode(st):
    pass
```

---

### Solution 1


```python
vow = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}

def encode(st):
    for w in vow:
        st = st.replace(w, vow[w])
    return st

def decode(st):
    for k,v in vow.items():
        st = st.replace(v, k)
    return st
```



### Solution 2


```python
def encode(st, t=str.maketrans("aeiou", "12345")):
    return st.translate(t)

def decode(st, t=str.maketrans("12345", "aeiou")):
    return st.translate(t)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53697be005f803751e0015aa/)
