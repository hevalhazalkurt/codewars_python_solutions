# CodeWars Python Solutions

---

## All Star Code Challenge # 18

This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

```python
strCount('Hello', 'o') // => 1
strCount('Hello', 'l') // => 2
strCount('', 'z')      // => 0
```

Notes:

* The first argument can be an empty string
* The second string argument will always be of length 1

---

### Given Code


```python
def str_count(strng, letter):
    pass
```

---

### Solution


```python
def str_count(strng, letter):
    return strng.count(letter)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5865918c6b569962950002a1/)
