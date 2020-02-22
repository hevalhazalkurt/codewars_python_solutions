# CodeWars Python Solutions

---

## Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence


Replace all vowel to exclamation mark in the sentence. `aeiouAEIOU` is vowel.

**Examples**

```python
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
```



---

### Given Code


```python
def replace_exclamation(s):
    pass
```

---

### Solution


```python
def replace_exclamation(s):
    return "".join(["!" if c in "aeiouAEIOU" else c for c in s])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/)
