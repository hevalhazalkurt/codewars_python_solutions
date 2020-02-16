# CodeWars Python Solutions

---

## The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.

**Examples**

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

---

### Given Code


```python
def generate_hashtag(s):
    pass
```

---

### Solution


```python
def generate_hashtag(s):
    return "#" + "".join([w.strip().title() for w in s.split()]) if 140 > len(s) > 1 else False
```


---


[See on CodeWars.com](https://www.codewars.com/kata/52449b062fb80683ec000024/)
